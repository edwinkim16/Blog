from flask import render_template,redirect,url_for,request,abort,flash
from .requests import get_quotes
from . import main
from flask_login import login_required
from ..models import User

@main.route('/')
def index():
    quote = get_quotes()
   
    return render_template('index.html',quote=quote)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
