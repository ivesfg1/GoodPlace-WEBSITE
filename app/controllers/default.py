from flask import render_template
from app import goodplace


@goodplace.route('/')
@goodplace.route('/index')
def index():
    return render_template('index.html')

@goodplace.route('/login')
def login():
    return render_template('login.html')

@goodplace.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@goodplace.route('/home')
def home():
    return render_template('home.html')
