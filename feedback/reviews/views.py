from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm

# Create your views here.

def review(request):
    if request.method == 'POST':
        #entered_username = request.POST['username'] # {name:value}
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data) # {formKey: value}
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form":form
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")