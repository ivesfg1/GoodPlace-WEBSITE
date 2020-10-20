from flask_wtf import FlaskForm
# from flask_uploads import UploadSet, IMAGES

from werkzeug.utils import secure_filename

from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


# images = UploadSet('images', IMAGES)


class LoginForm(FlaskForm):
  
  email = StringField('Email', validators=[Length(min=6), Email(message='Use um email válido!'), DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])


class CadastroForm(FlaskForm):
  
  photo = FileField('Image')
  username = StringField('UserName', validators=[DataRequired()])
  name = StringField('Name', validators=[DataRequired()])
  email = StringField('Email', validators=[Length(min=6), Email(message='Use um email válido!'), DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])


class RequestForm(FlaskForm):

  about = TextAreaField('About', validators=[Length(max=418), DataRequired()])
  requisition = StringField('Name', validators=[Length(max=50), DataRequired()])
