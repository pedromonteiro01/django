from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.review),
    path("thank-you", views.thank_you)
]
