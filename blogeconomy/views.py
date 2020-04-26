from blogeconomy.forms import User
from django.views.generic.edit import FormView

# Create your views here.
from django.http import Http404,HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import User


def registration (request):
    people = User.objects.all()
    return render(request, "mainApp/registrationpage.html",{"people": people})
def create(request):
    if request.method == "POST":
      tom = User()
      tom.Name = request.POST.get("name")
      tom.Category = request.POST.get("category")
      tom.Purpose=request.POST.get("purpose")
      tom.Password=request.POST.get("password")
      tom.Salary = request.POST.get("salary")
      tom.save()
    return HttpResponseRedirect("/")
