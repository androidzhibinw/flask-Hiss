from app import db


class Items(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    reproduce_steps = db.Column(db.String, nullable=False)
    crs = db.Column(db.String)
    jiras = db.Column(db.String)
    log_analysis = db.Column(db.String)
    solution_desc = db.Column(db.String)
    gerrits = db.Column(db.String)
    create_date = db.Column(db.DateTime, server_default=db.func.now())
    updated_date = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __init__(self, title, reproduce_steps, crs, jiras, log_analysis, solution_desc, gerrits):
        self.title = title
        self.reproduce_steps = reproduce_steps
        self.crs = crs
        self.jiras = jiras
        self.log_analysis = log_analysis
        self.solution_desc = solution_desc
        self.gerrits = gerrits

    def __repr__(self):
        return 'title:' + self.title + '\n'
