from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    author = StringField("Автор", validators=[DataRequired()])
    genre = StringField("Жанр")
    condition = SelectField("Состояние", choices=[("new", "Новая"), ("used", "Б/у")])
    description = TextAreaField("Описание")
    submit = SubmitField("Добавить книгу")
