from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired
from wtforms import ValidationError, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed

LEN_MAP = {
    '1': '< 3 miles',
    '2': '3 ~ 5 miles',
    '3': '5 ~ 8 miles',
    '4': '8 ~ 10 miles',
    '5': '>10 miles',
    '6': 'not sure'
}

def get_lenth_range(choice):
    if choice in LEN_MAP:
        return LEN_MAP[choice]
    raise ValueError("Unknown choice:" + choice)

class AddSpotForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    desc = TextAreaField('Description')
    length_selection = SelectField('Length in miles', choices=sorted(LEN_MAP.items()))
    image = FileField('Thumbnail Image')
    submit = SubmitField('Submit')
