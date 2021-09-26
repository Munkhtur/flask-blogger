from flaskblog import create_app
from flaskblog.models import Tag
from flaskblog import db

app = create_app()

@app.context_processor
def context_processor():
    tags = Tag.query.all()
    for tag in tags:
        if not tag.posts:
            db.session.delete(tag)
            db.session.commit()
    return dict(tags=tags)

if __name__ == '__main__':
    app.run(debug=True)
