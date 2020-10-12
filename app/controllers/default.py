from flask import render_template
from app import goodplace


@goodplace.route('/', defaults={'user': None})
@goodplace.route('/index/<user>')
def index(user):
    return render_template('index.html', user=user)
