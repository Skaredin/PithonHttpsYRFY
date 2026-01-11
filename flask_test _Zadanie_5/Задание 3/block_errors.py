class BlockErrors:
    def __init__(self, errors):
        """
        errors: set типов исключений, которые нужно игнорировать
        """
        self.errors = tuple(errors)  # преобразуем в tuple для isinstance

    def __enter__(self):
        # ничего не делаем при входе
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        exc_type: тип исключения
        exc_val: объект исключения
        exc_tb: traceback
        """
        if exc_type is None:
            # исключения нет
            return False
        if issubclass(exc_type, self.errors):
            # исключение нужно игнорировать
            return True
        # исключение не ожидаемое → прокидываем дальше
        return False
