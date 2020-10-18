from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, logout_user, login_required, current_user
from app import goodplace, db, lm

from app.models.forms import LoginForm, CadastroForm
from app.models.tables import User, Request


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for('index'))


@goodplace.route('/')
@goodplace.route('/index')
def index():
    return render_template('index.html')


@goodplace.route('/login', methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            flash("Este email não está cadastrado!")
        
        else:
            if user.password == form.password.data:
                login_user(user)
                return redirect(url_for("home"))
            else:
                flash("A senha está incorreta!")
    return render_template('login.html', form=form)


@goodplace.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))


@goodplace.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = CadastroForm()
    if form.validate_on_submit():
        
        existing_email = User.query.filter_by(email=form.email.data).first()
        existing_username = User.query.filter_by(email=form.email.data).first()

        if existing_email and existing_username is None:
            user = User(username=form.username.data, name=form.name.data, email=form.email.data, 
            password=form.password.data, about='Olá! Estou cadastrado no GoodPlace!')
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login"))
        else:
            flash("Já existe um usuário cadastrado com este email ou nome de usuário!")

    else:
        print(form.errors)
    return render_template('cadastrar.html', form=form)


@goodplace.route('/home')
@login_required
def home():
    return render_template('home.html')
