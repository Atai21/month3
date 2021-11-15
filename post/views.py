import datetime
import random

from django.shortcuts import render
from django.http import HttpResponse

def hello_world_view(request):
    return HttpResponse("Hello, World!")

def date_view(request):
    now = datetime.datetime.now()
    return HttpResponse(str(now))

def random_view(request):
    ran = random.randint(0, 100)
    return HttpResponse(str(ran))