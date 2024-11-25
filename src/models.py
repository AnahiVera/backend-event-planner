from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    profile = db.relationship('Profile', backref="user")

    def serialize(self):
        return {
            "id":self.id,
            "username":self.username,
            "is_active":self.is_active,
            "profile": self.profile.serialize()
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

