from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import  current_user, login_required
from flaskblog.posts.forms import PostForm
from flaskblog.models import Post
from flaskblog.models import Tag
from flaskblog import db
import bleach


posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():
        content = bleach.clean(form.content.data, tags= bleach.sanitizer.ALLOWED_TAGS + ['h1','p', 'br'], attributes=bleach.sanitizer.ALLOWED_ATTRIBUTES)
        post = Post(title = form.title.data, content=content, author=current_user)
        for tag in form.tags.data:
            if tag:
                tag_db = Tag.get_or_create(tag)
                post.tags.append(tag_db)
        db.session.add(post)
        db.session.commit()
        flash('Post created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend="New Post")

@posts.route('/post/<string:post_slug>')
def post(post_slug):
    post = Post.query.filter_by(slug = post_slug).first_or_404()

    return render_template('post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    form = PostForm()
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    if form.validate_on_submit():
        post.title = form.title.data
        content = bleach.clean(form.content.data, tags= bleach.sanitizer.ALLOWED_TAGS + ['h1','p', 'br'], attributes=bleach.sanitizer.ALLOWED_ATTRIBUTES)
        post.content = content
        for tag in form.tags.data:
            if tag:
                tag_db = Tag.get_or_create(tag)
                post.tags.append(tag_db)
        db.session.commit()
        flash('Post updated', 'success')
        return redirect(url_for('posts.post', post_slug= post.slug))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post', post_id=post.id, tags = post.tags)
    

@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()

    flash('Post deleted', 'success')
    return redirect(url_for('main.home'))