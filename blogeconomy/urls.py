
from django.conf.urls import url
from django.urls import path
from . import views

app_name='blogeconomy'
urlpatterns=[
    path('', views.registration, name='registration'),
    path('create/', views.create),

             ]
