import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from rpgtools import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    f_name = random_hex + f_ext
    f_path = os.path.join(current_app.root_path, 'static/profile_pics', f_name)
    output_size = (256, 256)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(f_path)
    return f_name


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                    sender='noreply@example.com',
                    recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.grant_reset', token=token, _external=True)}

If you did not make this request, simply ignore this email.
'''
    mail.send(msg)


