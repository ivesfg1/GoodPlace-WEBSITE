from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
  
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])


class CadastroForm(FlaskForm):
  
  username = StringField('Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  is_admin = BooleanField('Admin', validators=[DataRequired()])
