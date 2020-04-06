from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class myform(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastame', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    gender =SelectField('Gender', choices=[('Male', 'male'),('Female','female')],validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[DataRequired()])
    image = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg','png'], 'Images only!')])
