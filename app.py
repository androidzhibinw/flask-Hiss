from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'random string'
db = SQLAlchemy(app)
CsrfProtect(app)


from view import items_blueprint

app.register_blueprint(items_blueprint)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)


