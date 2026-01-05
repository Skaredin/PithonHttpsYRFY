from flask import Flask
app = Flask(__name__)
# 🔹 Глобальный список машин (НЕ пересоздаётся)
cars = ["Chevrolet", "Renault", "Ford", "Lada"]

@app.route("/")
def index():
    return """
    <h1>Главная страница</h1>
    <ul>
        <li><a href="/hello_world">Привет, мир</a></li>
        <li><a href="/cars">Список машин</a></li>
    </ul>
    """
@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"

@app.route("/cars")
def cars_list():
    # превращаем список в строку через запятую
    return ", ".join(cars)

if __name__ == "__main__":
    app.run(debug=True)
