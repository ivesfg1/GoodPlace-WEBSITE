from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class LoginForm(FlaskForm):
  
  email = StringField('Email', validators=[Length(min=6), Email(message='Use um email válido!'), DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])


class CadastroForm(FlaskForm):
  
  username = StringField('UserName', validators=[DataRequired()])
  name = StringField('Name', validators=[DataRequired()])
  email = StringField('Email', validators=[Length(min=6), Email(message='Use um email válido!'), DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])