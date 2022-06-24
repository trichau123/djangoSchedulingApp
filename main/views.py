from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
	return HttpResponse("<h1> login </h1>")

def pSchedule(response):
	return HttpResponse("<h1> schedule page </h1>")

def lgin(request):
	return render(request, 'index.html',{})