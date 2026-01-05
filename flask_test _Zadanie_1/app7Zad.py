from flask import Flask, request, redirect
from random import choice
from datetime import datetime, timedelta
import os
import re
app = Flask(__name__)
cars = ["Chevrolet", "Renault", "Ford", "Lada"]
cats = [
    "корниш-рекс",
    "русская голубая",
    "шотландская вислоухая",
    "мейн-кун",
    "манчкин"
]
words_list = []  # Глобальная переменная для слов из книги
book_file_path = None  # Абсолютный путь к выбранному файлу
@app.route("/")
def index():
    return f"""
    <h1>Главная страница</h1>
    <ul>
        <li><a href="/hello_world">Привет, мир</a></li>
        <li><a href="/cars">Список машин</a></li>
        <li><a href="/cats">Случайная порода кошек</a></li>
        <li><a href="/get_time/now">Текущее время</a></li>
        <li><a href="/get_time/future">Время через час</a></li>
        <li><a href="/select_book">Выбрать книгу</a></li>
        <li><a href="/get_random_word">Случайное слово из книги</a></li>
        <li><a href="/counter">Счётчик посещений</a></li>
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
    current_time = datetime.now()
    return f"Точное время: {current_time}"
@app.route("/get_time/future")
def get_time_future():
    now = datetime.now()
    current_time_after_hour = now + timedelta(hours=1)
    return f"Точное время через час будет {current_time_after_hour}"

# Задача 6: выбор книги
@app.route("/select_book", methods=["GET", "POST"])
def select_book():
    global words_list, book_file_path
    if request.method == "POST":
        # Получаем путь, который ввёл пользователь
        file_path = request.form.get("book_path")
        if not os.path.isabs(file_path):
            # Если путь относительный, делаем абсолютным относительно текущего файла
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(BASE_DIR, file_path)
        if os.path.exists(file_path):
            book_file_path = file_path
            words_list = load_words(book_file_path)
            return f"Книга загружена! {len(words_list)} слов готово к использованию.<br><a href='/'>Главная</a>"
        else:
            return f"Файл не найден: {file_path}<br><a href='/select_book'>Попробовать снова</a>"
    # GET-запрос — форма для ввода пути
    return """
    <h2>Выберите файл книги</h2>
    <form method="post">
        Путь до файла: <input type="text" name="book_path" style="min-width: 100%;" placeholder="war_and_peace.txt">
        <input type="submit" value="Загрузить">
    </form>
    <br><a href="/">Главная</a>
    """
def load_words(file_path):
    """Читает файл, возвращает список слов без знаков препинания"""
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
    # Убираем все символы кроме букв и цифр
    words = re.findall(r'\b\w+\b', text)
    return words
@app.route("/get_random_word")
def get_random_word():
    if not words_list:
        return "Сначала выберите книгу! <a href='/select_book'>Выбрать книгу</a>"
    return choice(words_list)
# Задача 7: Сколько раз открывалась данная страница
@app.route("/counter")
def counter_page():
    counter_page.visits += 1
    return f"Страница /counter открыта {counter_page.visits} раз(а)"

# Инициализация счётчика
counter_page.visits = 0



if __name__ == "__main__":
    app.run(debug=True)
