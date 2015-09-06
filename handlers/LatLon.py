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


#Google places api key : AIzaSyDkCJ6oDH1z7-rgDT3P5be9wkkvUSE4fP8

class LatLon(BaseHandler):
	def get(self):
		ulat = self.request.get('ulat')
		ulat = math.radians(Decimal(ulat))
		
		ulon = self.request.get('ulon')
		#self.response.out.write(ulat*2)
		#self.response.out.write(ulon)
		ulon  = math.radians(Decimal(ulon))
		ran = self.request.get('ran')
		vendordata = db.GqlQuery("SELECT * FROM VendorData").fetch(limit=10)

		output = []
		for vendor in vendordata:
			vlat =math.radians(vendor.latitude)
			vlon = math.radians(vendor.longitude)
			R = 6373.0

			dlon = vlon - ulon
			dlat = vlat - ulat

			a = sin(dlat / 2)**2 + cos(ulat) * cos(vlat) * sin(dlon / 2)**2
			c = 2 * atan2(sqrt(a), sqrt(1 - a))

			dist = R*c
			
			if int(dist) < int(ran):
				output.append(vendor.vid)

		result=[]
		for v in output:
			vendordata = db.GqlQuery("SELECT * FROM VendorData WHERE vid=  :y",y=v).get()
			obj = {
			'vendorname' : vendordata.vendorname,
			'vendorfullname' : vendordata.vendorfullname,
			'vendoremail' : vendordata.vendoremail,
			'vid': vendordata.vid,
			'latitude': vendordata.latitude,
			'longitude':vendordata.longitude
			}
			result.append(obj)

		#req = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(ulat)+','+str(ulon)+'&radius=5000&types=food&key=AIzaSyDkCJ6oDH1z7-rgDT3P5be9wkkvUSE4fP8')
		self.response.out.write(json.dumps(result))
		#self.response.out.write(json.dumps("------"))
		#self.response.out.write(json.dumps(req.json()))