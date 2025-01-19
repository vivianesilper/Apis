from db import db

class PurchaseOrdersModel(db.Model):
    __tablename__ = 'purchase_order'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    
    def __init__(self, description):
        self.description = description
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        
    @classmethod
    def find_all(cls):
        return cls.query.all() # select * from purchase_order
    
    @classmethod
    def find_by_id(cls, __id):
        return cls.query.filter_by(id=__id).first():
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
        