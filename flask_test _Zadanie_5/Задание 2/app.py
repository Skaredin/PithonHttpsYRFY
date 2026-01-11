from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField
from wtforms.validators import DataRequired, NumberRange
import subprocess
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
class CodeForm(FlaskForm):
    code = TextAreaField("Code", validators=[DataRequired()])
    timeout = IntegerField(
        "Timeout",
        validators=[
            DataRequired(),
            NumberRange(min=1, max=30)
        ]
    )
@app.route("/run", methods=["POST"])
def run_code():
    form = CodeForm()

    if not form.validate_on_submit():
        return jsonify({"error": "Invalid input"}), 400

    code = form.code.data
    timeout = form.timeout.data

    cmd = [
        "prlimit",
        "--nproc=1:1",
        "python3",
        "-c",
        code
    ]
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(timeout=timeout)
        return jsonify({
            "stdout": stdout,
            "stderr": stderr
        })
    except subprocess.TimeoutExpired:
        process.kill()
        return jsonify({
            "error": "Execution time exceeded"
        }), 408
