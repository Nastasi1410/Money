from blogeconomy.forms import User
from django.views.generic.edit import FormView
from django import forms
from blogeconomy import forms

# Create your views here.
from django.http import Http404,HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from blogeconomy.models import User,Mainclass
from datetime import datetime
def page_user(request):
   if request.method == "GET":

    Userpassword = request.GET.get("password")
    Login=request.GET.get("login")
    usern = User.objects.get(Password__exact=Userpassword, Name__exact=Login)
    Now=datetime.now()

    return render(request,"mainApp/userpage.html",{'Usern': usern,'Date':Now})
def write(request):
    if request.method == "POST":
        date=datetime.now()
        spend=Mainclass()
        spend.Categoryspend = 'category1'
        spend.Sum=request.POST.get("category1")
        spend.Dateofspend=date
        spend.ID_User_id = request.POST.get('Usern')
        spend.save()
        return HttpResponseRedirect("/")