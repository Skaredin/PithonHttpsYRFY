import pytest
from freezegun import freeze_time
from app import app, GREETINGS
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
# Функция для получения ожидаемого greeting по фиксированной дате
def expected_greeting_for_date(year, month, day):
    from datetime import datetime
    weekday = datetime(year, month, day).weekday()
    return GREETINGS[weekday]

def test_can_get_correct_username_with_weekdate(client):
    # фиксируем дату, например, среда, 3 января 2024
    with freeze_time("2024-01-03"):  # это среда
        name = "Саша"
        response = client.get(f'/hello-world/{name}')
        assert response.status_code == 200
        # проверяем имя
        assert f'Привет, {name}' in response.get_data(as_text=True)
        # проверяем день недели
        expected_greeting = expected_greeting_for_date(2024, 1, 3)
        assert expected_greeting in response.get_data(as_text=True)

def test_greeting_does_not_conflict_with_username(client):
    # случай, когда имя похоже на день недели
    with freeze_time("2024-01-05"):  # пятница
        name = "Хорошей среды"
        response = client.get(f'/hello-world/{name}')
        assert response.status_code == 200
        # имя корректно отображается
        assert f'Привет, {name}' in response.get_data(as_text=True)
        # день недели правильный (пятница)
        expected_greeting = expected_greeting_for_date(2024, 1, 5)
        assert expected_greeting in response.get_data(as_text=True)
