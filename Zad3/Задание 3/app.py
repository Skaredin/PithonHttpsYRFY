from flask import Flask, abort
from collections import defaultdict

app = Flask(__name__)

# структура: storage[year][month][day] = total_expense
storage = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))


@app.route("/add/<date>/<int:number>")
def add_expense(date, number):
    """
    Добавление траты за конкретный день.
    date: 'YYYYMMDD'
    number: сумма в рублях
    """
    if len(date) != 8 or not date.isdigit():
        return "Некорректный формат даты! Используйте YYYYMMDD", 400

    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])

    if not (1 <= month <= 12) or not (1 <= day <= 31):
        return "Некорректный месяц или день!", 400

    storage[year][month][day] += number
    return f"Добавлено {number} руб. на дату {year}-{month:02}-{day:02}"


@app.route("/calculate/<int:year>")
def calculate_year(year):
    """
    Сумма трат за весь год
    """
    year_data = storage.get(year)
    if not year_data:
        return f"За {year} нет записей", 404

    total = sum(
        day_expense
        for month_data in year_data.values()
        for day_expense in month_data.values()
    )
    return f"Сумма расходов за {year}: {total} руб."


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year, month):
    """
    Сумма трат за конкретный месяц
    """
    year_data = storage.get(year)
    if not year_data:
        return f"За {year} нет записей", 404

    month_data = year_data.get(month)
    if not month_data:
        return f"За {year}-{month:02} нет записей", 404

    total = sum(month_data.values())
    return f"Сумма расходов за {year}-{month:02}: {total} руб."


if __name__ == "__main__":
    app.run()
