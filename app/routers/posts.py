from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from app import db
from app.forms.posts import PostForm
from app.forms.comments import CommentForm
from app.models.posts import Post
from app.models.comments import Comment

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@posts_bp.route('/posts')
@login_required
def my_posts():
    posts = Post.query.filter_by(author_id=current_user.id).all()
    return render_template('index.html', posts=posts, show_actions=True)


@posts_bp.route('/<int:id>')
def post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('The post was not found!')
        return redirect(url_for('posts.index'))
    form = PostForm()
    comment_form = CommentForm()
    form.title.data = post.title
    form.content.data = post.content
    return render_template('post.html', form=form, post=post, comment_form=comment_form, current_user=current_user)


@posts_bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!')
        return redirect(url_for('posts.my_posts'))
    return render_template('create.html', form=form)


@posts_bp.route('/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('The post was not found!')
        return redirect(url_for('posts.my_posts'))

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.my_posts'))

    comment_form = CommentForm()
    form.title.data = post.title
    form.content.data = post.content
    return render_template('post.html', title='Edit Post', form=form, post=post, comment_form=comment_form,
                           current_user=current_user, edit=True)


@posts_bp.route('/<int:id>/delete')
@login_required
def delete(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('The post was not found!')
        return redirect(url_for('posts.my_posts'))

    title = post.title
    Comment.query.filter_by(post_id=post.id).delete()
    db.session.delete(post)
    db.session.commit()
    flash('"{}" was successfully deleted!'.format(title))
    return redirect(url_for('posts.my_posts'))
