from flask import Blueprint, redirect, url_for, flash
from flask_login import current_user, login_required
from app import db
from app.forms.comments import CommentForm
from app.models.posts import Post
from app.models.comments import Comment

comments_bp = Blueprint('comments', __name__)


@comments_bp.route('/<int:id>/add-comment', methods=['POST'])
@login_required
def add_comment(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('The post was not found!')
        return redirect(url_for('posts.index'))

    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(post_id=id, content=form.content.data, author_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('posts.post', id=post.id))

