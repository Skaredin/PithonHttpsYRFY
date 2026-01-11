import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False
    with app.test_client() as client:
        yield client


def test_timeout(client):
    response = client.post("/run", data={
        "code": "import time; time.sleep(5)",
        "timeout": 1
    })

    assert response.status_code == 408


def test_invalid_data(client):
    response = client.post("/run", data={
        "code": "",
        "timeout": 100
    })

    assert response.status_code == 400


def test_shell_injection(client):
    response = client.post("/run", data={
        "code": 'print("ok"); echo hacked',
        "timeout": 5
    })

    data = response.json
    assert "hacked" not in data.get("stdout", "")
