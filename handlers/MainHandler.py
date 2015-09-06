from imports import *
from config import *
from routes import *
from handlers import *
from models import *
import json

class MainHandler(BaseHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'application/json'
		current_url = self.request.url
		username = current_url.split('/')[4]
		userdata = db.GqlQuery("SELECT * FROM UserData WHERE username= :u",u=username).get()

		obj = {
		'username' : userdata.username,
		'fullname' : userdata.fullname,
		'email' : userdata.email
		}
		self.response.out.write(json.dumps(obj))