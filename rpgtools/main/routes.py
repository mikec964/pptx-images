from flask import render_template, url_for, flash, redirect, request, Blueprint
from rpgtools.models import Post
from rpgtools.main.forms import UploadPPTXForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/pptix", methods=['GET', 'POST'])
def pptix():
    form = UploadPPTXForm()
    if form.validate_on_submit():
        flash('Your file has been accepted.', 'success')
        return redirect(url_for('main.home'))
    return render_template('pptix.html', title='Powerpoint Image Extractor',
                            form=form)


