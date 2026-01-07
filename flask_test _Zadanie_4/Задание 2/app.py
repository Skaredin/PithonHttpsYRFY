from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email

from hw2_validators import number_length, NumberLength

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False
app.config["SECRET_KEY"] = "secret"


class RegistrationForm(FlaskForm):
    email = StringField(
        validators=[
            InputRequired(message="Email обязателен"),
            Email(message="Неверный формат email")
        ]
    )

    # Используем ФУНКЦИОНАЛЬНЫЙ валидатор
    phone = IntegerField(
        validators=[
            InputRequired(message="Телефон обязателен"),
            number_length(min=10, max=10, message="Телефон должен содержать 10 цифр")
        ]
    )

    # Можно заменить на КЛАССОВЫЙ вариант:
    # phone = IntegerField(
    #     validators=[
    #         InputRequired(),
    #         NumberLength(min=10, max=10)
    #     ]
    # )

    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()  # необязательное поле


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        return (
            f"Пользователь {form.email.data} "
            f"успешно зарегистрирован, телефон +7{form.phone.data}"
        )

    return f"Ошибка валидации: {form.errors}", 400


if __name__ == "__main__":
    app.run(debug=True)
