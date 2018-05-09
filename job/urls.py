'''from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name="index"),
]	

from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register
urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register),
]
'''
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
	path('', views.front, name ='front'),
	path('add', views.addjob, name ='addjob'),
	path('jobpage', views.joblist, name ='joblist'),
    path('detail', views.home, name='home'),
    path('register', views.register_page, name='registerpage'),
    path('login', views.login_page, name='loginpage'),

]