# -*- coding: utf_8 -*-
'''
Created on 2019/1/29
------------------------------------------------------
データ保存用のModelを管理
------------------------------------------------------
@author: ken
'''
from google.appengine.ext import ndb

    
class Sales_item(ndb.Model):
    Menu = ndb.StringProperty()
    Price = ndb.IntegerProperty()
    Num = ndb.IntegerProperty()
    Disc = ndb.IntegerProperty()
    Total = ndb.IntegerProperty()
    
class Sales(ndb.Model):
    Sales_No = ndb.StringProperty()
    Sales_Date = ndb.DateProperty()
    Sales_Time = ndb.DateTimeProperty()
    Sales_Total = ndb.IntegerProperty()
    Sales_Amount =  ndb.IntegerProperty()
    Sales_Tax = ndb.IntegerProperty()
    Rec_Method = ndb.StringProperty()
    Rec_DiscTicket = ndb.IntegerProperty()
    Stylist = ndb.StringProperty()
    items = ndb.StructuredProperty(Sales_item,repeated=True)