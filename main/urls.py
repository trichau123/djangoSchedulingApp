from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [

#path("", views.lgin, name = "lgin"),
path("index/", user_views.index, name = "home-page"),
path("register/", user_views.register, name = "register"),
path("", auth_views.LoginView.as_view(template_name= 'signin.html'), name = "signin"),
path("signout/", auth_views.LogoutView.as_view(), name = "signout"),
#path("register", register, name=" register"),

]
#start