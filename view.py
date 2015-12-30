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
#view one,
@items_blueprint.route('/item/<id>')
def item(id=None):
    item = Items.query.get(id)
    return render_template('item.html',item=item)
#updtae
@items_blueprint.route('/item/<id>/update',methods=['GET','POST'])
def item_update(id=None):
    item = Items.query.get(id)
    form = ItemForm(request.form)
    if request.method == 'POST' and form.validate():
        #print 'update post',form.title,form.reproduce_steps,form.crs,form.jiras,form.log_analysis,form.solution_desc,form.gerrits
        item.title = form.title.data
        item.reproduce_steps = form.reproduce_steps.data
        item.crs = form.crs.data
        item.jiras = form.jiras.data
        item.log_analysis = form.log_analysis.data
        item.solution_desc = form.solution_desc.data
        item.gerrits = form.gerrits.data
        try:
            db.session.commit()
            flash("update "+ id + " success!")
        except Exception as e:
            flash("update:" +str(e))
        return redirect(url_for('.home'))
    else:
        if not item:
            flash("id=" + id + " does not exist..")
            return redirect(url_for('.home'))
        form.title.data = item.title
        form.reproduce_steps.data=item.reproduce_steps
        form.crs.data = item.crs
        form.jiras.data = item.jiras
        form.log_analysis.data = item.log_analysis
        form.solution_desc.data = item.solution_desc
        form.gerrits.data = item.gerrits
        return render_template('update.html', form=form,item=item)
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
@items_blueprint.route('/item/<id>/delete',methods=['POST'])
def item_del(id=None):
    item = Items.query.filter_by(id=id)
    #print item
    try:
        item.delete()
        db.session.commit()
        flash("item id="+id+" deleted!")
    except Exception as e:
        flash(e)
    return redirect(url_for('.home'))
