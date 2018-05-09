from django.shortcuts import render
from .models import job_listing
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django import forms
from .forms import RegistrationForm
from job.forms import *
from django.contrib.auth import login, authenticate

# Create your views here.
def front(request):
    return render(request, 'job/frontpage.html' )

 


def addjob(request):

    job_lists = job_listing.objects.all()
    context = {'job_detail':job_lists}

    if request.method == "POST":
        tit = request.POST.get("title","")
        des = request.POST.get("description","")

        job_list =job_listing.objects.create(

            title =  tit,
            description = des
            )
        job_list.save()

        return render(request, 'job/addjob.html', context)


    return render(request, 'job/addjob.html', context)     


     

def home(request):

	job_lists = job_listing.objects.all()
	context = {'job_detail':job_lists}

	if request.method == "POST":
		tit = request.POST.get("title","")
		des = request.POST.get("description","")

		job_list =job_listing.objects.create(

			title =  tit,
			description = des
			)
		job_list.save()

		return render(request, 'job/index.html', context)


	return render(request, 'job/index.html', context)


def joblist(request):

    job_lists = job_listing.objects.all()
    context = {'job_detail':job_lists}

    if request.method == "POST":
        tit = request.POST.get("title","")
        des = request.POST.get("description","")

        job_list =job_listing.objects.create(

            title =  tit,
            description = des
            )
        job_list.save()

        return render(request, 'job/joblist.html', context)


    return render(request, 'job/joblist.html', context)





'''

def login_page(request):
    user_lists = user_detail.objects.all()
    context = {'user_detail':user_lists}

    if request.method == "POST":
        uname = request.POST.get("username","")
        upass = request.POST.get("password","")

        user_list =user_detail.objects.create(

            title =  uname,
            description = upass
            )
        user_list.save()

        return render(request, 'registration/login.html', context)


    return render(request, 'register/login.html', context)
'''

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            user.save()
            return HttpResponseRedirect('/')

            
    form = RegistrationForm()
    variables =  {'form': form}
    return render(request, 'registration/register.html', variables)    	



def login_page(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('/')
    form = Loginform()
    variables =  {'form': form}
    return render(request, 'registration/login.html', variables) 




'''    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form' : form})
    '''