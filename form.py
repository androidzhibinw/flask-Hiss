from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

class ItemForm(Form):
    title = TextField('Title',validators=[DataRequired()])
