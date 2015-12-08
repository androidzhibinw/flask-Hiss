from app import db


class Items(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    reproduce_steps = db.Column(db.String, nullable=False)
    crs = db.Column(db.String,nullable=False)
    jiras = db.Column(db.String,nullable=False)
    log_analysis = db.Column(db.String,nullable=False)
    solution_desc = db.Column(db.String, nullable=False)
    gerrits = db.Column(db.String,nullable=False)
    create_date = db.Column(db.DateTime,nullable=False)
    update_date = db.Column(db.DateTime,nullable=False)
    
    def __init__(self, title,reproduce_steps, crs,jiras,log_analysis,solution_desc,gerrits,c_date,u_date):
        self.title = title
        self.reproduce_steps = reproduce_steps
        self.crs = crs
        self.jiras = jiras
        self.log_analysis = log_analysis
        self.solution_desc = solution_desc
        self.gerrits = gerrits
        self.create_date = c_date
        self.update_date = u_date
    def __repr__(self):
        return 'title:' + self.title +'\n'
