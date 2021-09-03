from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound 

challenges = {
    "january":"january challenge",
    "february":"february challenge",
    "march":"march challenge",
    "april":"april challenge",
    "may":"may django challenge",
    "june":"june challenge",
    "july":"july challenge",
    "august":"august challenge",
    "september":"september challenge",
    "october":"october challenge",
    "november":"november challenge",
    "december":"december challenge",
}

# Create your views here.

#view: takes a request and sents back a response
def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not suported!')