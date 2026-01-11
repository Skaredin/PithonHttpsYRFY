rom flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField
from wtforms.validators import DataRequired, NumberRange
class CodeForm(FlaskForm):
    code = TextAreaField(
        "Code",
        validators=[DataRequired()]
    )
    timeout = IntegerField(
        "Timeout",
        validators=[
            DataRequired(),
            NumberRange(min=1, max=30)
        ]
    )
