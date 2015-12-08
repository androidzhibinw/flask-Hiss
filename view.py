from flask import render_template, Blueprint,\
        request,flash, redirect, url_for

items_blueprint = Blueprint(
        '/',__name__,
        template_folder='templates'
        )


from model import Items
@items_blueprint.route('/')
def home():
    items = Items.query.all()
    return render_template('home.html',items=items)

@items_blueprint.route('/item/<id>')
def item(id=None):
    item = Items.query.get(id)
    return render_template('item.html',item=item)
