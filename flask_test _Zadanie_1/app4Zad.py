from flask import Flask
from random import choice
from datetime import datetime

app = Flask(__name__)

# 🔹 Глобальный список машин (НЕ пересоздаётся)
cars = ["Chevrolet", "Renault", "Ford", "Lada"]

# 🔹 Глобальный список пород кошек (НЕ пересоздаётся)
cats = [
    "корниш-рекс",
    "русская голубая",
    "шотландская вислоухая",
    "мейн-кун",
    "манчкин"
]


@app.route("/")
def index():
    return """
    <h1>Главная страница</h1>
    <ul>
        <li><a href="/hello_world">Привет, мир</a></li>
        <li><a href="/cars">Список машин</a></li>
        <li><a href="/cats">Случайная порода кошек</a></li>
        <li><a href="/get_time/now">Текущее время</a></li>
    </ul>
    """


@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"


@app.route("/cars")
def cars_list():
    return ", ".join(cars)


@app.route("/cats")
def cats_random():
    return choice(cats)


@app.route("/get_time/now")
def get_time_now():
    # получаем текущее время
    current_time = datetime.now()

    # форматируем строку через переменную
    return f"Точное время: {current_time}"


if __name__ == "__main__":
    app.run(debug=True)
