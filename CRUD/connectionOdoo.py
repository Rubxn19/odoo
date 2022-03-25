
from contextlib import nullcontext
from itertools import product
from django.shortcuts import render
from django.http import HttpResponse, response
# import requests
import xmlrpc.client
import json
import base64
import sys
import json 
import os
# from dotenv import load_dotenv
# load_dotenv()

class connectionOdoo():
    models = None
    common = None
    output = None
    uid = None
    url =  ""
    db = ""
    password = ""
    user = ""
    def __init__(self, *args):
        self.url = "http://localhost:8069"
        self.db =  "MnK"
        self.password =  "fundillo"
        self.user =  "Ruben_OrtizPadilla@outlook.com"
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.output = self.common.version()
        self.uid = self.common.authenticate(self.db, self.user , self.password, self.output)