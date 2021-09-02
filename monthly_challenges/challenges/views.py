from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

# first view: takes a request and sents back a response
def index(request):
    return HttpResponse("This works!")
