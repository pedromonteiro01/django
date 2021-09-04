from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december":None,
}

# Create your views here.
def index(request):
    months = [m for m in challenges.keys()]
    
    return render(request, "challenges/index.html", {
        "months":months
    })


#view: takes a request and sents back a response
def monthly_challenge_by_number(request, month):
    months = [m for m in challenges.keys()] #[january, february, march, ...]
    
    if  month > len(months):
        return HttpResponseNotFound("Invalid Month!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            "text":challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
    
# render() always render a success page!