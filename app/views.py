from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!!")

def index(request):
    return HttpResponse("Hello World!!")

def trial(request):
    return HttpResponse("Changes from Dishan")

def sum(request):
    return HttpResponse("SUM")