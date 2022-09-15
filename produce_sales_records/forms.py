from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    quantity = StringField("Quantity/kg", validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    date = StringField("Date", validators=[DataRequired()])
    market = StringField("Market", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    submit = SubmitField("Insert")