
from imports import *
from config import *
from routes import *
from handlers import *
from models import *
import json


class UserHandler(BaseHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'application/json'
		current_url = self.request.url
		uid = current_url.split('/')[4]
		userdata = db.GqlQuery("SELECT * FROM UserData WHERE uid= :u",u=uid).get()

		obj = {
		'username' : userdata.username,
		'fullname' : userdata.fullname,
		'email' : userdata.email,
		'uid': userdata.uid
		}
		self.response.out.write(json.dumps(obj))

