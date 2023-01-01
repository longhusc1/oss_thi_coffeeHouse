from flask import redirect, render_template, url_for, flash, request
from apps import db, app, photos
from .models import Category, addsp
from .forms import Addsp
import secrets
from datetime import datetime


@app.route('/addCate', methods=['GET', 'POST'])
def addCate(): #Thêm loại
    if request.method=="POST":
        getcate = request.form.get('cate')
        cate = Category(name=getcate)
        db.session.add(cate)
        flash(f'Loại {getcate} đã được thêm vào database', 'success')
        db.session.commit()
        return redirect(url_for('addCate'))
    return render_template('sanpham/addCate.html')


@app.route('/addSp', methods=['GET', 'POST'])
def addSp():
    form = Addsp(request.form)
    categories = Category.query.all()
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        decs = form.discription.data
        image = photos.save(request.files.get('image'), name=secrets.token_hex(10)+ ".")
        date = datetime.now()
        category = request.form.get('category')
        
        addSanpham = addsp(name=name,price=price,decs = decs, pub_date=date, 
        category_id= category ,image=image)
        db.session.add(addSanpham)
        flash(f'{name} đã được thêm vào database', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    
    return render_template('sanpham/addsp.html', form=form, title="Thêm sản phẩm", categories=categories)