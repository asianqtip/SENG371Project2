'''This file details the directory of pages of the application and the operations of each page'''
import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, UploadForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
import subprocess


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    entries = os.listdir(os.path.join(app.root_path, 'static/datasets'))
    if request.method == 'POST':
        algo = os.path.join(app.root_path, 'static/algorithms', request.values.get('algorithms'))
        datapath = os.path.join(app.root_path, 'static/datasets', request.values.get('dataset'))
        filename = os.path.join(app.root_path, 'static/results', request.values.get('dataset'))
        flash('Processed!', 'success')
        subprocess.call(['python', algo, datapath, filename])
        return redirect(url_for('home'))
    return render_template('home.html', posts=posts, entries=entries, legend='New Algorithm')

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = form_picture.filename
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    form_picture.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)

def save_alg(form_alg):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_alg.filename)
    alg_fn = random_hex + f_ext
    alg_path = os.path.join(app.root_path, 'static/algorithms', alg_fn)
    form_alg.save(alg_path)

    return alg_fn

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        alg_filename = save_alg(form.alg.data)
        #fileName = secure_filename(form.alg.data.filename)
        #file_path = os.path.join(app.root_path, 'static/algorithms', fileName)
        #f.save(file_path)
        #form.alg.data.save(os.path.join(app.root_path, 'static/algorithms', fileName))
        post = Post(title=form.title.data, alg_file = alg_filename, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your algorithm has been posted!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Algorithm',
                           form=form, legend='New Algorithm')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

"""@app.route("/run", methods=['GET', 'POST'])
@login_required
def run():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    entries = os.listdir(os.path.join(app.root_path, 'static/datasets'))
    if request.method == 'POST':
        algo = os.path.join(app.root_path, 'static/algorithms', request.values.get('algorithms'))
        datapath = os.path.join(app.root_path, 'static/datasets', request.values.get('dataset'))
        filename = os.path.join(app.root_path, 'static/results', request.values.get('dataset'))
        flash('Files selected', 'success')
        subprocess.call(['python', algo, datapath, filename])
        return redirect(url_for('run'))
    return render_template('run.html', posts=posts, entries=entries, legend='New Algorithm')
    """


@app.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        form.data_file.data.save(os.path.join(app.root_path, 'static/datasets', form.data_file.data.filename))
        flash('Your file has been uploaded', 'success')
        return redirect(url_for('upload'))
    return render_template('upload.html',form=form, legend='Upload Dataset')

@app.route("/results", methods=['GET'])
def results():
    entries = os.listdir(os.path.join(app.root_path, 'static/results'))
    result_path = os.path.join(app.root_path, 'static/results')
    return render_template('results.html', entries=entries, legend='Results', result_path=result_path)
