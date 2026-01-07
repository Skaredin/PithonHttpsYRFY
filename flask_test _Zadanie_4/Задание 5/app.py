from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/ps", methods=["GET"])
def ps():
    errors = []
    # получаем аргументы списком
    args = request.args.getlist("arg")
    if not args:
        errors.append("Нет аргумента. ?arg=a&arg=u&arg=x")
    if errors:
        return {"errors": errors}, 400
    # формируем команду БЕЗ shell=True
    command = ["ps"] + args
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except Exception as e:
        return {"errors": [str(e)]}, 400

    if result.stderr:
        return {"errors": [result.stderr]}, 400

    return f"<pre>{result.stdout}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
