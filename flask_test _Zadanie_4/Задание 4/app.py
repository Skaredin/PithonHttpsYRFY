from flask import Flask
import subprocess

app = Flask(__name__)


def get_uptime() -> str:
    """
    Возвращает uptime системы в читаемом виде
    """
    
    result = subprocess.run(
        ["uptime", "-p"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

   
    uptime_str = result.stdout.strip()

    
    if uptime_str.startswith("up "):
        uptime_str = uptime_str[3:]

    return uptime_str


@app.route("/uptime", methods=["GET"])
def uptime():
    uptime_value = get_uptime()
    return f"Текущее время безотказной работы составляет {uptime_value}"


if __name__ == "__main__":
    app.run(debug=True)
