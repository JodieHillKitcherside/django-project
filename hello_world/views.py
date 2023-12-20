from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def about(request):
    return HttpResponse("This would be the about page")

def index(request):

   if request.method == "POST":
       return HttpResponse("You must have POSTed something")
   else:
    return  HttpResponse(request.method)