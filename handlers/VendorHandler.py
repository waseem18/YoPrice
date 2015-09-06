from imports import *
from config import *
from routes import *
from handlers import *
from models import *
import json
from google.appengine.api import search




#class VendorHandler(BaseHandler):
#	def get(self):
#		self.render('input.html')
#
#	def post(self):
#		vn = self.request.get('vendorname')
#		vf = self.request.get('vendorfullname')
#		ve = self.request.get('vendoremail')
#		lat = self.request.get('lat')
#		lat = float(lat)
#		lon = self.request.get('long')
#		lon = float(lon)
#
#		instance = VendorData(vendorfullname=vf,vendoremail=ve,vendorname=vn,latitude=lat,longitude=lon)
#		instance.put()
#		vid = instance.key().id()
#		instance.vid = str(vid)
#		instance.put()
#		self.response.out.write("DONE")




class VendorHandler(BaseHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'application/json'
		current_url = self.request.url
		vid = current_url.split('/')[4]
		vendordata = db.GqlQuery("SELECT * FROM VendorData WHERE vid= :u",u=vid).get()

		obj = {
		'vendorname' : vendordata.vendorname,
		'vendorfullname' : vendordata.vendorfullname,
		'vendoremail' : vendordata.vendoremail,
		'vid': vendordata.vid,
		'latitude': vendordata.latitude,
		'longitude':vendordata.longitude
		}
		self.response.out.write(json.dumps(obj))