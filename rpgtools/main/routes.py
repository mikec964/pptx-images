from flask import (Blueprint, current_app, flash, redirect, render_template,
                     request, url_for)
import os
from ..pptimgx.pptimgx import Pptimgx
import secrets
from rpgtools.models import Post
from rpgtools.main.forms import UploadPPTXForm
from rpgtools.users.utils import save_picture, send_reset_email

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
        if form.pptx.data:
            # save the pptx
            pptx_dir = os.path.join(current_app.root_path, 'static/pptx')
            original_f_name = form.pptx.data.filename
            f_base = secrets.token_hex(8)
            f_name = f_base + '.pptx'
            f_path = os.path.join(pptx_dir, f_name)
            form.pptx.data.save(f_path)
            # import the pptx, save pics in a folder
            pres1 = Pptimgx(f_path)
            pic_dir = os.path.join(pptx_dir, f_base)
            os.mkdir(pic_dir)
            for p in range(pres1.nPics):
                pres1.save(p, path=pic_dir)   # 'image 1.png'
            flash(f'Your file {original_f_name} has been accepted.', 'success')
        return redirect(url_for('main.home'))
    return render_template('pptix.html', title='Powerpoint Image Extractor',
                            form=form)

