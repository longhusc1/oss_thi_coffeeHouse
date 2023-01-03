from apps import db, app
from datetime import datetime
import json

class Khachhang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    taikhoan = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    address = db.Column(db.String(150), unique=True, nullable=False)
    matkhau = db.Column(db.String(180), unique=False, nullable=False)
    def __repr__(self):
        return '<Khachhang %r>' % self.taikhoan

class JsonEcodedDict(db.TypeDecorator):
    impl = db.Text
    def set_value(self, value, dialect):
        if value is None:
             return '{}'
        else: 
            return json.dumps(value)
    def get_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)


class KhachhangOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hoadon = db.Column(db.String(20), unique=True, nullable=False)
    trangthai = db.Column(db.String(20), default='Chờ duyệt', nullable=False)
    khachhang_id = db.Column(db.Integer, unique=False, nullable=False)
    ngaytao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    orders = db.Column(JsonEcodedDict)

    def __repr__(self):
        return '<KhachhangOrder %r>' % self.hoadon

with app.app_context():
    db.create_all()