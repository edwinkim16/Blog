from flask import render_template,redirect,url_for
from .requests import get_quotes
from . import main
from flask_login import login_required

@main.route('/')
def index():
    quote = get_quotes()
   
    return render_template('index.html',quote=quote)
