from flask import render_template, Blueprint,\
        request,flash, redirect, url_for

items_blueprint = Blueprint(
        '/',__name__,
        template_folder='templates'
        )


from model import Items
from form import ItemForm
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
        return redirect(url_for('.home'))
    else:
       return render_template('add.html', form=form)
#delete
