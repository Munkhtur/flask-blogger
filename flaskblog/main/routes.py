from functools import wraps
from flask import Blueprint, request, render_template, redirect, g
from flask.helpers import url_for
from flaskblog.models import Post
from flaskblog.models import Tag
from flask_login import current_user

main = Blueprint('main', __name__)


@main.context_processor
def myFunc():
    def myFunc(text):
        return text[0:200]
    return dict(myFunc= myFunc)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/latest")
def latest():
    posts = Post.query.order_by(Post.date_posted.desc()).limit(5)
    return render_template('latest.html', posts=posts, title="latest")

@main.route('/my_posts')
def my_posts():
    if current_user.is_authenticated:
       return  redirect(url_for('users.user_posts', username=current_user.username))
    else:
        return redirect(url_for('users.login'))