from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Оптимальный вариант — КОРТЕЖ (минимум памяти, порядок важен)
weekdays = (
    "понедельника",
    "вторника",
    "среды",
    "четверга",
    "пятницы",
    "субботы",
    "воскресенья"
)


@app.route("/hello-world/<name>")
def hello_world(name):
    weekday_number = datetime.today().weekday()  # 0–6
    day_name = weekdays[weekday_number]
    return f"Привет, {name}. Хорошего {day_name}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
