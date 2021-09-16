from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm

# Create your views here.

# https://docs.djangoproject.com/en/3.2/topics/http/file-uploads/
def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form":form
        })

    def post(self, request): #when submit the form
        #handle the upload file
        submitted_form = ProfileForm(request.POST, request.FILES)
        
        if submitted_form.is_valid():   
            store_file(request.FILES['image'])
            return HttpResponseRedirect("/profiles")
        
        return render(request, "profiles/create_profile.html", {
            "form": submitted_form
        })
