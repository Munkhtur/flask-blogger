
from operator import pos
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flaskblog.models import Tag
from flaskblog.models import Post
from flask import Blueprint, request
from flaskblog import db




tags = Blueprint('tags', __name__)


@tags.route('/tags/<string:tag_name>')
def tag_posts(tag_name):
    tag = Tag.query.filter_by(name = tag_name).first()
    posts = sorted(tag.posts, key=lambda p: p.date_posted, reverse=True)
    return render_template('tag_posts.html', posts = posts)

@tags.route('/tags/<int:post_id>/<string:tag>')
def remove_frompost(post_id, tag):
    post = Post.query.get_or_404(post_id)
    tag_obj = Tag.query.filter_by(name=tag).first()
    post.tags.remove(tag_obj)
    db.session.commit()
    return redirect(url_for('posts.update_post', post_id=post_id))
