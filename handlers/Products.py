from imports import *
from config import *
from routes import *
from handlers import *
from models import *
import json
import math
from decimal import Decimal
from math import sin, cos, sqrt, atan2, radians
from google.appengine.api import search




class Products(BaseHandler):
	def get(self):
		dataa = db.GqlQuery("SELECT * FROM Products").fetch(limit=10)
		output = []
		for data in dataa:
			obj = {
			'pid':data.pid,
			'vid':data.vid,
			'pimg':data.pimg,
			'pname':data.pname,
			'pdetail':data.pdetail,
			'ptype':data.ptype,
			'availability':data.availability,
			'quantity': data.quantity
			}
			output.append(obj)
		self.response.out.write(json.dumps(output))