# Create your views here.

from django.template.context import RequestContext
from django.shortcuts import render_to_response

from django.http import HttpResponse

from django.db.models import Count, Min, Max, Sum, datetime

from drpharmacy.models import *

from datetime import date

import json


def home(request):
    context = RequestContext(request)
    context.update({ 'msg_body' : "List of all machines", })
    
    products = Product.objects.all()
    context.update({ 'products' : products, })
    return render_to_response("home.html", context_instance=context)
