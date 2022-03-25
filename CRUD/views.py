
import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import 
from django.urls import reverse
# from dotenv import load_dotenv
from .connectionOdoo import connectionOdoo


# Create your views here.

def index(request):
    
    odoo = connectionOdoo()
    
    products = odoo.models.execute_kw(odoo.db,odoo.uid,odoo.password,
    'product.template','search_read',
        [
            [
                [ "company_id" ,"=", 1   ]
            ]
        ],
        {'fields': ["name", "list_price", "default_code","description_picking"]}
    )
    return render(request, "crud/index.html", {"mnk": products})


    
# Create your views here.
