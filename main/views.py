from django.shortcuts import render, redirect
from django.http import HttpResponse
#check user and pass
from django.contrib.auth import authenticate,  login,logout
#added jul6
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#create user
#from django.contrib.auth import User
# Create your views here.

#index is home page
def index(request):
	return render(request, 'calendar.html')
	#return HttpResponse("<h1> calendar </h1>")


def pSchedule(response):
	return HttpResponse("<h1> schedule page </h1>")

#def lgin(request):
#	return render(request, 'index.html',{})
#
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			#create user in admin
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}!')
			return redirect('home-page')
	else:
		form =UserCreationForm()
	return render(request, 'register.html', {'form': form})
#message.debug, message.info, message.success, message.warning,
#message.error
#connect with index html
def signin(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user is  not None:
			login(request, user)
			redirect( 'pSchedule')

		else:
			messages.error(request, "Bad Credentials")
			return  redirect('')

	return render(request,"signin.html")

@login_required
def home(request):
	return render(request, 'calendar.html')
