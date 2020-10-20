import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'um-nome-bem-seguro'

# Configurações para envio de arquivos (fotos)

UPLOAD_FOLDER = '/home/ives/PycharmProjects/goodplace/app/static'