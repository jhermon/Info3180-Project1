from . import db
import datetime


class userProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    location = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    date = db.Column(db.String(255))
    image = db.Column(db.String(255))


    def _intit_(self,firstname ,lastname, email, gender, location, bio,date, image):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.gender = gender
        self.location = location
        self.bio = bio
        self.date= date
        self.image = image
   
   
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