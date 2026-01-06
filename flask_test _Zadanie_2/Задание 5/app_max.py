from flask import Flask, abort
app = Flask(__name__)
@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    # numbers — это строка вида "10/2/9/1"
    parts = numbers.split("/")
    valid_numbers = []

    for part in parts:
        try:
            # пытаемся преобразовать в число (целое)
            num = int(part)
            valid_numbers.append(num)
        except ValueError:
            # если не число — игнорируем
            continue

    if not valid_numbers:
        return "Нет переданных чисел!", 400  # возвращаем ошибку

    max_num = max(valid_numbers)
    return f"Максимальное число: {max_num}"


if __name__ == "__main__":
    app.run()
