from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

class AddSpotForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()
    location = StringField('Location', validators=[DataRequired()
    desc = TextAreaField('Address')
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])