from flask import Flask, abort
import os
app = Flask(__name__)
@app.route("/preview/<int:size>/<path:relative_path>")
def preview_file(size, relative_path):
    # получаем абсолютный путь
    abs_path = os.path.abspath(relative_path)
    # проверка, что файл существует
    if not os.path.isfile(abs_path):
        return f"Файл не найден: {abs_path}", 404

    try:
        # открываем файл в текстовом режиме
        with open(abs_path, "r", encoding="utf-8") as f:
        # читаем только первые SIZE символов
            text = f.read(size)             
    except Exception as e:
        return f"Ошибка при чтении файла: {e}", 500

    result_size = len(text)
    # формируем HTML
    response = f"<b>{abs_path}</b> {result_size}<br>{text}"
    return response
if __name__ == "__main__":
    app.run()
