from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy
import model


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


@app.route('/')
def index():
    items = model.Items.query.all()
    return render_template('home.html',items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)


