'''
Created on 2018/04/30

@author: ken
'''
import webapp2
import os
import Cookie
import hashlib
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from __builtin__ import True
import cloudstorage as gcs
import logging
from google.appengine.api import app_identity

class MainPage(webapp2.RequestHandler):
    def get(self):

        # Setup the Drive v3 API
        SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('drive', 'v3', http=creds.authorize(Http()))

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            text = "No item exist"
        else:
            text = "No item exist"
            for item in items:
                text = text + item['name']

        template_values = {"text":text}
        path = os.path.join(os.path.dirname(__file__), './templates/index.html')
        self.response.out.write(template.render(path, template_values))
        return

app = webapp2.WSGIApplication([('/',MainPage)]
                              ,debug=True)