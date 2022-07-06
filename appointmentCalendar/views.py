from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def appCalendar(request):
	return render(request,'calendar/calendar.html')