from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange

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

    phone = IntegerField(
        validators=[
            InputRequired(message="Телефон обязателен"),
            NumberRange(
                min=1000000000,
                max=9999999999,
                message="Телефон должен содержать 10 цифр"
            )
        ]
    )

    name = StringField(
        validators=[InputRequired(message="Имя обязательно")]
    )

    address = StringField(
        validators=[InputRequired(message="Адрес обязателен")]
    )

    index = IntegerField(
        validators=[
            InputRequired(message="Индекс обязателен"),
            NumberRange(min=1, message="Индекс должен быть числом")
        ]
    )

    comment = StringField()  


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data
        phone = form.phone.data
        return f"Пользователь {email} успешно зарегистрирован и имеет номер телефона +7{phone}"

    return f"Неверный ввод, {form.errors}", 400


if __name__ == "__main__":
    app.run(debug=True)
