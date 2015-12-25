from flask_wtf import Form
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired

class ItemForm(Form):
    title = StringField('Title',validators=[DataRequired()])
    reproduce_steps = TextAreaField('Reproduce Steps',validators=[DataRequired()])
    crs = StringField('CRs')
    jira = StringField('Jiras')
    log_analysis = TextAreaField('Log Analysis')
    solution_desc = TextAreaField('Solution')
    gerrits = StringField('Gerrits')

