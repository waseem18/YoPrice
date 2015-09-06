from imports import *
from config import *
from routes import *
from handlers import *
from models import *
import json

class ProductsOfAVendor(BaseHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'application/json'
		current_url = self.request.url
		vid = current_url.split('/')[4]
		pdata = db.GqlQuery("SELECT * FROM Products WHERE vid= :v",v=vid).fetch(limit=10)

		output = []
		for item in pdata:
			obj = {
			'pid' : item.pid,
			'pname' : item.pname,
			'pdetail' : item.pdetail,
			'pimg' : item.pimg,
			'availability': item.availability,
			'quantity' : item.quantity,
			'pprice' : item.pprice,
			'ptype' : item.ptype,
			'vid': item.vid
			}
			output.append(obj)
		self.response.out.write(json.dumps(output))
