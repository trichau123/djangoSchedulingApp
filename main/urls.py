from django.urls import path
from . import views

urlpatterns = [

path("", views.lgin, name = "lgin"),
path("index/", views.index, name = "index"),
path("home/", views.pSchedule, name = "pSchedule"),

]
#start