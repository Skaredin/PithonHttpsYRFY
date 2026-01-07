from typing import Optional
from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    """
    Функциональный валидатор длины числа
    """

    def _number_length(form: FlaskForm, field: Field):
        if field.data is None:
            return

        value = str(field.data)

        if not value.isdigit():
            raise ValidationError(message or "Значение должно быть числом")

        length = len(value)

        if length < min or length > max:
            raise ValidationError(
                message or f"Длина числа должна быть от {min} до {max} цифр"
            )

    return _number_length


class NumberLength:
    """
    Валидатор длины числа в виде класса
    """

    def init(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def call(self, form: FlaskForm, field: Field):
        if field.data is None:
            return

        value = str(field.data)

        if not value.isdigit():
            raise ValidationError(self.message or "Значение должно быть числом")

        length = len(value)

        if length < self.min or length > self.max:
            raise ValidationError(
                self.message or f"Длина числа должна быть от {self.min} до {self.max} цифр"
            )
