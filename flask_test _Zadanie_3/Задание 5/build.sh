# --- Настройка ---
# Укажите ваши файлы
CODE_FILE="decrypt.py"         # основной код
TEST_FILE="test_decrypt.py"    # тесты

# --- Установка зависимостей ---
echo "=== Installing dependencies ==="
python3 -m pip install --upgrade pip
python3 -m pip install pylint pytest > /dev/null 2>&1

# --- Статический анализатор ---
echo "=== Running Pylint ==="
pylint "$CODE_FILE" --output-format=json > pylint_report.json
pylint_exit=$?

# Краткий отчёт и оценка
echo "=== Pylint Summary ==="
pylint "$CODE_FILE" --reports=y --score=y

if [[ $pylint_exit -ne 0 ]]; then
    echo "Статический анализатор обнаружил ошибки!"
    pylint_ok=0
else
    pylint_ok=1
fi

# --- Запуск тестов ---
echo "=== Running Tests ==="
python3 -m unittest "$TEST_FILE"
test_exit=$?

# --- Итог ---
if [[ $test_exit -eq 0 && $pylint_ok -eq 1 ]]; then
    echo "ОК"
    exit 0
else
    echo "Имеются ошибки"
    exit 1
fi
