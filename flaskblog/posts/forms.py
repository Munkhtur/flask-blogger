from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired , Length
from wtforms import StringField, SubmitField, TextAreaField
from .tag_form_field import TagListField

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', id="summernote" ,validators=[DataRequired()])
    tags = TagListField("Tags", separator=",", validators=[Length(max=8, message="You can only use up to 8 tags.")], filters = [lambda x: x or None])
    submit = SubmitField('Post') 