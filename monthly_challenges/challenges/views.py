from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound 

# Create your views here.

# first view: takes a request and sents back a response
def january(request):
    return HttpResponse("This works!")

def february(request):
    return HttpResponse("Walk for at least 20min!")


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Eat no meat for the entire month'
    elif month == 'february':
        challenge_text = 'Walk for 20min'
    elif month == 'march':
        challenge_text = 'Learn django'
    else:
        return HttpResponseNotFound('This month is not suported!')
    return HttpResponse(challenge_text)