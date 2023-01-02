from flask import redirect, render_template, url_for, flash, request,session,current_app
from apps import db, app, photos
from apps.sanpham.models import addsp

@app.route('/addcart', methods=['POST'])
def addcart():
    try:
        sanpham_id = request.form.get('sanpham_id')
        quantity= request.form.get('quantity')
        sanpham = addsp.query.filter_by(id=sanpham_id).first()
        # if sanpham_id and quantity and request.method =="POST":
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)
