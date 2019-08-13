from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from subprocess import Popen, PIPE, STDOUT
import json
from scraper import run_scraper_module
# Create your views here.

# Landing Page
def index(request):
    return render(request, 'main/index.html')

# Filtered Company search table
def searchTable(request):
    return HttpResponse('The search table Page')

# Company summary page
def summary(request, company_id):
    return HttpResponse(f'Summary page for company {company_id}')

# Run scraper
# def run_scraper(request):
#     # command = ['python3', '/home/mcsadmin/webServer/scraper/app.py']
#     # try: 
#     #     process = Popen(command, stdout=PIPE, stderr=STDOUT)
#     #     output = process.stdout.read()
#     #     exitStatus = process.poll()
#     #     response = {'output':str(output)}
#     #     if exitStatus is 0:
#     #         response['status'] = 'Success'
#     #     else:
#     #         response['status'] = 'Failed'
#     # except Exception as e:
#     #     response = {"status": "failed", "output":str(e)}
    
#     # responseBack = HttpResponse(json.dumps(response), content_type='application/json', status=200)
#     # return responseBack
#     response = {'status':'Success'}
#     return (HttpResponse(json.dumps(response), content_type='application/json', status=200))
#     # run_scraper_module()
