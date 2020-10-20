import os, base64

from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, logout_user, login_required, current_user

from werkzeug.utils import secure_filename

from app import goodplace, db, lm

from app.models.forms import LoginForm, CadastroForm, RequestForm
from app.models.tables import User, Request, Help


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for('index'))


@goodplace.route('/')
@goodplace.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

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
            if user.check_password(password=form.password.data):
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
        existing_name = User.query.filter_by(username=form.username.data).first()

        if existing_name is None:
            if existing_email is None:

                photo = form.photo.data
                filename = secure_filename(photo.filename)
                path = os.path.join(goodplace.config['UPLOAD_FOLDER'], filename)
                photo.save(path)
                
                user = User(username=form.username.data, name=form.name.data, email=form.email.data, photo=filename)
                
                user.set_password(password=form.password.data)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("login"))
            else:
                flash("Já existe um usuário cadastrado com este email!")
        else:
            flash("Já existe um usuário cadastrado com este nome de usuário!")

    return render_template('cadastrar.html', form=form)


@goodplace.route('/home')
@login_required
def home():

    helps = Help.query.all()
    request = Request.query.all()

    return render_template('home.html', request=request, helps=helps)


@goodplace.route('/perfil/<int:id>', methods=['GET', 'POST'])
def perfil(id):
    
    user = User.query.get(id)
    requests = Request.query.filter_by(user_id=id).all()
    helps = Help.query.all()

    form = RequestForm()
    if form.validate_on_submit():

        request = Request(requisition=form.requisition.data, about=form.about.data, user_id=id)
        
        db.session.add(request)
        db.session.commit()

        flash("Pedido cadastrado com sucesso.")
        return redirect(url_for('perfil', id=id))

    return render_template('perfil.html', user=user, requests=requests, form=form, id=id, helps=helps)


@goodplace.route('/request/<int:id>', methods=['GET', 'POST'])
def request(id):

    requests = Request.query.filter_by(user_id=current_user.id).all()
    request = Request.query.get(id)
    
    form = RequestForm()

    # form.about.data = request.about
    # form.requisition.data = request.requisition

    if form.validate_on_submit():
        
        request.about = form.about.data
        request.requisition = form.requisition.data

        db.session.commit()

        flash("Pedido atualizado com sucesso.")
        return redirect(url_for('perfil', id=request.user_id))

    return render_template('request.html', request=request, requests=requests, form=form, id=id)


@goodplace.route('/request/<int:id>/help', methods=['GET', 'POST'])
def help(id):

    request = Request.query.get(id)

    help = Help(user_id=current_user.id, request_id=request.id)
    db.session.add(help)
    db.session.commit()

    return redirect(url_for('home'))
    return render_template('home.html', id=request.id, request=request)
