## Simple flask application with CRUD
### use virtualenv 
#### why use virtualenv ? 
virtualenv is used to resolve  multiple Python projects using different versions of python or python libraries.
virtualenv can create isolated Python environments as you wish.
learn more about it from [virtualenv](https://virtualenv.readthedocs.org)

#### install virtualenv 

    sudo pip install virtualenv
    mkdir myproject
    cd myproject
    virtualenv venv (name venv whatever you like)
    source venv/bin/activate  (active venv)
    deactivate (deactive venv)

refer [flask-virtualenv](http://flask.pocoo.org/docs/0.10/installation/#virtualenv)

### active venv and install Flask

    source venv/bin/activate 
    pip install Flask 

### install Flask-SQLAlChemy

    source venv/bin/activate
    pip install Flask-SQLAlchemy

## Simple hello world of Flask
### hello world web app , refer [Flask_Hello_World](http://flask.pocoo.org/docs/0.10/quickstart/)

    touch app.py

input below code:

    from flask import Flask
    @app.route('/')
    def index():
        return 'hello world'

    if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)

run it, you will see it in your browser `youip:5000`:

    python app.py
## try something with database using SQLAlchemy

### more than sql

while you can use sql to create database and tables like below:

    sqlite3 app.db < schema.sql

here i come to use SQLAlchemy, first time use SQLAlchemy, have installed it prevously.
The right place for use SQLAlchemy in flask read [here](http://flask-sqlalchemy.pocoo.org/)

### create SQLAlchemy  db

    from flask.ext.sqlalchemy import SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    db = SQLAlchemy(app)

use `pragma table_info(table_name)` to check table column info.

### create your model 
it is easy to create your model 

    from app import db
    class Post(db.Model):
        __tablename__='post'
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String,nullable=False)
        content=db.Column(db.String,nullable=False)
        def __init__(self,title,content):
            self.title = title
            self.content=content

where to create the table ? will create the models. refer [flask-sqlalchemy-api](http://flask-sqlalchemy.pocoo.org/2.1/api/)

    db.create_all()

### use Blueprint
#### why use Blueprint? refer [flask-blueprint](http://flask.pocoo.org/docs/0.10/blueprints/)

At first , you may write all your routes in the main py file , when it gets more and more, it's better to seperate them to different part.
Use Blueprint can help seperate handle different part urls in different module/file.

register blueprint in the main py file.

    app.register_blueprint(items_blueprint)

`items_blueprint` can handle related urls in its own module.

    items_blueprint = Blueprint(
            '/',__name__,
            template_folder='templates'
            )

    @items_blueprint.route('/')
    def home():
        items = Items.query.all()
        return render_template('home.html',items=items)
### use wtf 
#### why use [wtforms](http://wtforms.readthedocs.org/)  and [flask-wtf](http://flask-wtf.readthedocs.org/)? 

use wtfforms in flask make you handle form easily.

