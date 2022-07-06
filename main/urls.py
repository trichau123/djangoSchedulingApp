from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

#path("", views.lgin, name = "lgin"),
path("index/", views.index, name = "home-page"),
path("pSchedule/", views.pSchedule, name = "pSchedule"),
path("", auth_views.LoginView.as_view(template_name= 'signin.html'), name = "signin"),
path("signout/", auth_views.LogoutView.as_view(), name = "signout"),


]
#start