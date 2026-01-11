import pytest
from block_errors import BlockErrors
def test_ignore_error():
    # Ошибка игнорируется
    try:
        with BlockErrors({ZeroDivisionError}):
            a = 1 / 0
    except ZeroDivisionError:
        pytest.fail("ZeroDivisionError не должен был прокинуться")


def test_raise_error():
    # Ошибка прокидывается выше
    with pytest.raises(TypeError):
        with BlockErrors({ZeroDivisionError}):
            a = 1 / '0'


def test_nested_blocks():
    # Ошибка прокидывается внутри, но игнорируется снаружи
    outer = {TypeError, ZeroDivisionError}
    try:
        with BlockErrors(outer):
            inner = {ZeroDivisionError}
            with BlockErrors(inner):
                a = 1 / '0'  # TypeError, игнорируется внешним
    except TypeError:
        pytest.fail("TypeError должен быть пойман внешним блоком")


def test_child_exception_ignored():
    # Дочерние ошибки игнорируются
    try:
        with BlockErrors({Exception}):
            with BlockErrors({ZeroDivisionError}):
                a = 1 / '0'  # TypeError, игнорируется внешним
    except Exception:
        pytest.fail("Ошибка должна быть игнорирована внешним блоком")
