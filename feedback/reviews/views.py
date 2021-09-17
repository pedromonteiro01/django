from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView): #form class not needed
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
    def form_valid(self, form): # only if it is valid
        form.save()
        return super().form_valid(form)
        
    '''def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")'''

# Create your views here.
'''
def review(request):
    if request.method == 'POST':
        #entered_username = request.POST['username'] # {name:value}
        form = ReviewForm(request.POST) 
        
        if form.is_valid():
            #review = Review(
            #    user_name=form.cleaned_data['user_name'], 
            #    feedback = form.cleaned_data['review_text'], 
            #    rating = form.cleaned_data['rating'])
            #review.save()
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form":form
    })
'''

class ThankYouView(TemplateView):
    template_name = "reviews/thank-you.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['message'] = "This works!"
        
        return context
    

'''class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context'''

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review # just poiting, not instanciating
    context_object_name = "reviews"
    
    '''def get_queryset(self): # filtering data
        base_query =  super().get_queryset()
        data = base_query.filter(rating__gte=1) # rating>=1
        return data'''
    

'''class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context['review'] = selected_review
        return context
'''

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    # pk in urls to identify objects
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object # from official docs
        request = self.request # from official docs
        favorite_id = request.session.get("favorite_review") # get is better
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        
        return context
    
    
'''
def thank_you(request):
    return render(request, "reviews/thank_you.html")
'''

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id #any key can be used
        
        return HttpResponseRedirect('/reviews/'+review_id)