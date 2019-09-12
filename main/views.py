from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import ensure_csrf_cookie
from subprocess import Popen, PIPE, STDOUT
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt
import saving_data
# Create your views here.

# Landing Page
def index(request):
    return render(request, 'main/index.html')

# Filtered Company search table
def searchTable(request):
    return HttpResponse('The search table Page')

# Filter Page
def filter(request):
    return render(request, 'main/filter.html')

# Company summary page
def summary(request, ticker):
    company = get_object_or_404(Company, ticker=ticker) 
    price = company.price_set.latest('date')
    ratios = company.ratios_set.latest('date')
    directors = company.directors_set.filter
    profile = company.companyprofile_set.latest('date')
    #bokeh(import data)
    #create graph
    #get html
    #get js

    return render(request, 'main/summary.html', {'company': company, 'price': price, 'profile': profile, 'directors': directors, 'ratios': ratios})


# add filter information to db
@csrf_exempt
def postfilter(request):
    if request.method == 'POST':
        # data = eval(request.body.decode('utf-8'))
        data = eval(request.body.decode('utf-8'))
        Filter.objects.create(risk = data['risk'], index = data['index'], blacklist = data['blacklist'])
        return HttpResponse(data)


#confirmation of Scraping
@csrf_exempt #! This is NOT GOOD LONG TERM, WE NEED CSRF SECURITY!!!!!
def update(request):
    if request.method == 'GET':
        return HttpResponse('WRONG TYPE BUCKO, AINT NO GETS AROUND THIS PART OF TOWN')
    if request.method == 'POST':
        if request.FILES:
            data = request.FILES
            print(data)
            htmlData = 'You sent some files'
        elif request.body != "":
            data = request.body.decode('utf-8')
            saving_data.save_json_data(data)
            htmlData = 'You sent JSON data!'
            print(htmlData)
        else:
            htmlData = 'You didnt send anything'

        return render(request, 'main/updated.html',{'htmlData': htmlData})