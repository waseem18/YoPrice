from imports import *
from config import *
from routes import *
from handlers import *
from models import *
import json

class ProductHandler(BaseHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'application/json'
		current_url = self.request.url
		pid = current_url.split('/')[4]
		pdata = db.GqlQuery("SELECT * FROM Products WHERE pid= :p",p=pid).get()

		obj = {
		'pid' : pdata.pid,
		'pname' : pdata.pname,
		'pdetail' : pdata.pdetail,
		'pimg' : pdata.pimg,
		'availability': pdata.availability,
		'quantity' : pdata.quantity,
		'pprice' : pdata.pprice,
		'ptype' : pdata.ptype,
		'vid': pdata.vid
		}
		self.response.out.write(json.dumps(obj))
