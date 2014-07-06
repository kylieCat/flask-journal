from flask import render_template, redirect, request
from app import app, db
from app.models import Post
from app.forms import PostForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    posts = Post.query.all()
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(request.form['title'], request.form['body'])
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
    return render_template('index.html', posts=posts, form=form)