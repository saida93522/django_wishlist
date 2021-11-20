""" The App Engine Cron Service allows you to configure regularly scheduled tasks that operate at defined times or regular intervals. These tasks are commonly known as cron jobs. These cron jobs are automatically triggered by the App Engine Cron Service.
 
For this app: Invokes a GET request on scheduled time for any updates from an api"""

import requests
from .models import CatFacts
from django.http import HttpResponse

def get_cat_facts(request):
    response = request.get('https://catfact.ninja/fact').json()
    fact = response['fact']
    CatFact(fact=fact).save()
    return HttpResponse('ok')