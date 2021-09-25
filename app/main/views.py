from flask import render_template,redirect,url_for,request,abort,flash
from .requests import get_quotes
from . import main
from flask_login import login_required,current_user
from ..models import User
from .forms import UpdateProfile
from .. import db

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

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)