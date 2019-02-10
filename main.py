'''
Created on 2018/04/30

@author: ken
'''
import webapp2
import os
import models
from google.appengine.api import app_identity

import Cookie
import hashlib
from google.appengine.ext import db
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):

        path = os.path.join(os.path.dirname(__file__), './templates/index.html')
        self.response.out.write(template.render(path, ''))
        return
    
class Insert():
    def receive_item(self,js_item):
        
        newSales = models.Sales()
        newSales.Sales_No = "1"
        newSales.Sales_Amount = 100
        newItem = models.Sales_item()
        newItem.Menu = "Cut"
        newItem.total = 100
        newSales.items = [newItem,newItem]
        newSales.put()
 
        return

app = webapp2.WSGIApplication([('/',MainPage)]
                              ,debug=True)