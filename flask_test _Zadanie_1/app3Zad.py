from flask import Flask
from random import choice
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
    # каждый запрос — случайная порода
    return choice(cats)
if __name__ == "__main__":
    app.run(debug=True)
