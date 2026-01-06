import unittest
from app import app, storage
from collections import defaultdict

class TestFinanceApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Инициализация storage с тестовыми данными
        storage.clear()
        storage.update(defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
        storage[2026][1][1] = 100
        storage[2026][1][2] = 200
        storage[2026][2][1] = 300
        storage[2025][12][31] = 50

        # Flask test client
        cls.client = app.test_client()

    def test_add_valid_date(self):
        # Проверка добавления корректной даты
        response = self.client.get("/add/20260106/500")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Добавлено 500 руб.", response.get_data(as_text=True))
        # Проверка, что сумма добавилась
        self.assertEqual(storage[2026][1][6], 500)

    def test_add_invalid_date_format(self):
        # Некорректный формат даты
        response = self.client.get("/add/2026-01-06/100")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Некорректный формат даты", response.get_data(as_text=True))

    def test_add_invalid_month_or_day(self):
        # Некорректный месяц и день
        response = self.client.get("/add/20261301/100")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Некорректный месяц или день", response.get_data(as_text=True))

    def test_calculate_year_existing(self):
        # Сумма за существующий год
        response = self.client.get("/calculate/2026")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Сумма расходов за 2026: 1100 руб.", response.get_data(as_text=True))

    def test_calculate_year_empty(self):
        # Сумма за год без записей
        response = self.client.get("/calculate/2024")
        self.assertEqual(response.status_code, 404)
        self.assertIn("За 2024 нет записей", response.get_data(as_text=True))

    def test_calculate_month_existing(self):
        # Сумма за существующий месяц
        response = self.client.get("/calculate/2026/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Сумма расходов за 2026-01: 800 руб.", response.get_data(as_text=True))

    def test_calculate_month_empty_month(self):
        # Месяц без записей
        response = self.client.get("/calculate/2026/3")
        self.assertEqual(response.status_code, 404)
        self.assertIn("За 2026-03 нет записей", response.get_data(as_text=True))

    def test_calculate_month_empty_year(self):
        # Год без записей
        response = self.client.get("/calculate/2024/1")
        self.assertEqual(response.status_code, 404)
        self.assertIn("За 2024 нет записей", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
