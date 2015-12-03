from app import db

class Items(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    
    def __init__(self, title, description):
        self.title = title
        self.description = description
    def __repr__(self):
        return 'title:' + self.title

