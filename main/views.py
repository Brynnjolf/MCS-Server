from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from subprocess import Popen, PIPE, STDOUT
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# Landing Page
def index(request):
    return render(request, 'main/index.html')

# Filtered Company search table
def searchTable(request):
    return HttpResponse('The search table Page')

# Company summary page
def summary(request, ticker):
    company = get_object_or_404(Company, ticker=ticker) 
    price = company.price_set.latest('date')
    directors = company.directors_set.all()
    profile = company.companyprofile_set.latest('date')
    #bokeh(import data)
    #create graph
    #get html
    #get js

    return render(request, 'main/summary.html', {'company': company, 'price': price, 'profile': profile, 'directors': directors})

#confirmation of Scraping
@csrf_exempt #! This is NOT GOOD LONG TERM, WE NEED CSRF SECURITY!!!!!
def update(request):
    if request.method == 'GET':
        return HttpResponse('WRONG TYPE BUCKO, AINT NO GETS AROUND THIS PART OF TOWN')
    if request.method == 'POST':
        return render(request, 'main/updated.html',{'request': request})