from imports import *
from config import *
from routes import *
from handlers import *

class UserData(db.Model):
	uid = db.StringProperty()
	username = db.StringProperty()
	email = db.StringProperty()
	fullname = db.StringProperty()


class VendorData(db.Model):
	vid = db.StringProperty()
	latitude  = db.FloatProperty()
	longitude = db.FloatProperty()
	vendorname = db.StringProperty()
	vendoremail = db.StringProperty()
	vendorfullname = db.StringProperty()


class Products(db.Model):
	pid = db.StringProperty()
	vid = db.StringProperty()
	pname = db.StringProperty()
	pdetail = db.StringProperty()
	pimg = db.StringProperty()
	pprice = db.StringProperty()
	ptype = db.StringProperty()
	availability = db.StringProperty()
	quantity = db.StringProperty()