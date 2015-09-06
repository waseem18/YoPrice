from imports import *

config = {}
config['webapp2_extras.sessions'] = {'secret_key': 'RandomSecurityKey','cookie_args':{'max_age':86400}}