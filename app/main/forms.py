from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required,Email

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')