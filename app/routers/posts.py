from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app import db
from app.forms.posts import PostForm
from app.models.posts import Post

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@posts_bp.route('/<int:id>')
def post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('The post was not found!')
        return redirect(url_for('index'))
    else:
        return render_template('post.html', post=post)


@posts_bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!')
        return redirect(url_for('index'))
    return render_template('create.html', form=form)


@posts_bp.route('/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('The post was not found!')
        return redirect(url_for('index'))

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('index'))

    form.title.data = post.title
    form.content.data = post.content
    return render_template('profile.html', title='Edit Profile', form=form)


@posts_bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('The post was not found!')
        return redirect(url_for('index'))

    db.session.delete(post)
    db.session.commit()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
