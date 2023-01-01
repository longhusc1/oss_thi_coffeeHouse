
from wtforms import Form, DateField , IntegerField, StringField, BooleanField, TextAreaField, validators
from flask_wtf.file import FileAllowed, FileField, FileRequired
from datetime import datetime

class Addsp(Form):
    name = StringField('Tên',[validators.DataRequired()])
    price = IntegerField('Giá', [validators.DataRequired()])
    image = FileField('Ảnh', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    discription = TextAreaField('Mô tả', [validators.data_required()])