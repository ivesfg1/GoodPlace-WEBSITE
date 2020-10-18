from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, logout_user
from app import goodplace, db, lm

from app.models.forms import LoginForm, CadastroForm
from app.models.tables import User, Request


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@goodplace.route('/')
@goodplace.route('/index')
def index():
    return render_template('index.html')


@goodplace.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("home"))
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@goodplace.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))


@goodplace.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = CadastroForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, name=form.name.data, email=form.email.data, 
        password=form.password.data, about='Olá! Estou cadastrado no GoodPlace!')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    else:
        print(form.errors)
    return render_template('cadastrar.html', form=form)


@goodplace.route('/home')
def home():
    return render_template('home.html')
