from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.

# https://docs.djangoproject.com/en/3.2/topics/http/file-uploads/
def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request): #when submit the form
        #handle the upload file
        store_file(request.FILES['image'])
        return HttpResponseRedirect("/profiles")
