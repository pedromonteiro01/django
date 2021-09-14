from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm


# Create your views here.

def review(request):
    if request.method == 'POST':
        #entered_username = request.POST['username'] # {name:value}
        form = ReviewForm(request.POST) 
        
        if form.is_valid():
            '''review = Review(
                user_name=form.cleaned_data['user_name'], 
                feedback = form.cleaned_data['review_text'], 
                rating = form.cleaned_data['rating'])
            review.save()'''
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form":form
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")