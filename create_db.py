from app import db
from model import Items
import datetime

db.drop_all()
db.create_all()

#test data
dt=datetime.datetime.now()
item = Items('title1','rep_steps','cr1','jira1','loganalysis','solution','gerrits',dt,dt)
db.session.add(item)
db.session.commit()

