from flask_wtf import Form
from wtforms.validators import Required
from wtforms.fields import TextField, TextAreaField, SubmitField

class PostForm(Form):
    title = TextField('Title: ', validators=[Required('Every post needs a title.')])
    body = TextAreaField('Post Body: ', validators=[Required('Every post needs a body.')])
    submit = SubmitField('Save')
