from app import app

@app.route('/')
def index():
    return 'hello 123'
