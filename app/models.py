from . import db


class Property(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True)
    property_title = db.Column(db.String(128))
    rooms_number = db.Column(db.Integer)
    bedrooms_number = db.Column(db.Integer)
    price = db.Column(db.Float)
    property_type = db.Column(db.String(128))
    location = db.Column(db.String(128))
    photo_filename = db.Column(db.String(128))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
