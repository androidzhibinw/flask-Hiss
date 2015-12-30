from flask import render_template, Blueprint,\
        request,flash, redirect, url_for
from datetime import datetime

items_blueprint = Blueprint(
        '/',__name__,
        template_folder='templates'
        )


from model import Items
from form import ItemForm
from app import db
#view the list
@items_blueprint.route('/')
def home():
    items = Items.query.all()
    return render_template('home.html',items=items)
#view one , update
@items_blueprint.route('/item/<id>')
def item(id=None):
    item = Items.query.get(id)
    return render_template('item.html',item=item)
#add 
@items_blueprint.route('/item/add',methods=['GET','POST'])
def item_add():
    form = ItemForm(request.form)
    if request.method == 'POST' and form.validate():
        print 'get post',form.title,form.reproduce_steps,form.crs,form.jiras,form.log_analysis,form.solution_desc,form.gerrits
        try:
            dt = datetime.now()
            item = Items(form.title.data,form.reproduce_steps.data,form.crs.data,form.jiras.data,form.log_analysis.data,form.solution_desc.data,form.gerrits.data,dt,dt)
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            flash(e)
        return redirect(url_for('.home'))
    else:
       return render_template('add.html', form=form)
#delete
