from database.db import db
from util.utils import get_current_time

class Surroundings(db.Model):
    __tablename__= 'surroundings'

    id = db.Column(db.INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    indoor_tmp = db.Column(db.FLOAT)
    indoor_hmd = db.Column(db.FLOAT)
    time = db.Column(db.INTEGER)


    def __init__(self, indoor_tmp=24, indoor_hmd=64):
        self.indoor_tmp = indoor_tmp
        self.indoor_hmd = indoor_hmd
        self.time = get_current_time()

    
    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_latest_indoor():
        s = Surroundings.query.order_by(Surroundings.id.desc()).first()
        return [s.indoor_tmp,s.indoor_hmd,s.id]