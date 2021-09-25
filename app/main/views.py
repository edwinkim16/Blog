from flask import render_template,redirect,url_for,request,abort,flash
from .requests import get_quotes
from . import main
from flask_login import login_required,current_user
from ..models import User, Pitch, Comment
from .forms import UpdateProfile, PitchForm , CommentForm,SubscribeForm
from .. import db,photos

@main.route('/')
def index():
    quote = get_quotes()
    title = 'Blogs Site'
    pitch=Pitch.query.order_by(Pitch.id.desc()).all()
   
    return render_template('index.html',quote=quote, title= title,pitch=pitch)

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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))   

@main.route('/pitch/new', methods=['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():

        title=form.title.data
        content=form.content.data
        category=form.category.data
        pitch = Pitch(title=title, content=content,category=category)
        # pitch.save_pitch(pitch)
        db.session.add(pitch)
        db.session.commit()

        flash('Your pitch has been created!', 'success')
        return redirect(url_for('main.index', id=pitch.id))

    return render_template('new_pitch.html', title='New Post', pitch_form=form, post ='New Post')   

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        
        comment_content = form.comment.data
        

        comment = Comment(comment_content= comment_content,pitch_id=id)

        # pitch.save_pitch(pitch)
        db.session.add(comment)
        db.session.commit()
        
    comment = Comment.query.filter_by(pitch_id=id).all()
  


    return render_template('new_comment.html', title='New Post', comment=comment,comment_form=form, post ='New Post')     