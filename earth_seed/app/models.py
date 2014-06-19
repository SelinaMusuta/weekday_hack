from app import db

class Members(db.Model):
	id = db.Column(db.Integer, primary_key = True) 
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(120), unique =True)
	email = db.Column(db.String(50))
	password = db.Column(db.String(12))

	#def get_id(self):
	#	return unicode(self.id)

class Events(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(200))
	date = db.Column(db.DateTime)
	city = db.Column(db.String(150))
	attendance_count = (db.Integer)


