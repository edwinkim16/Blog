from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required,Email

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')



class PitchForm(FlaskForm):

    title = StringField('Blog title')
    category= SelectField('Blog Category', choices=[('Select a category', 'Select a category'),('Sports', 'Sports'),('Travel Blog', 'Travel Blog'),('Fitnes Blog', 'Fitness Blog')])
    content = TextAreaField('Blog content...')
    submit = SubmitField('Post')

class CommentForm(FlaskForm):

    comment = TextAreaField('Post Of The Comment')
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    subscriber_name = StringField('Enter your Full Name',validators=[Required()])
    subscriber_email = StringField('Enter your Email',validators=[Required(),Email()])
    submit = SubmitField('Subscribe')    

