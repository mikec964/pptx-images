from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class UploadPPTXForm(FlaskForm):
    pptx = FileField('Powerpoint Presentation',
                            validators=[DataRequired(), FileAllowed(['ppt', 'pptx'])])
    submit = SubmitField('Upload')


