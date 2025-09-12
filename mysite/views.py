from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")
def nav_bar(request):
    return render(request,"nav_bar.html")
def fotter(request):
    return render(request,"fotter.html")
def aboutUs(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def projects(request):
    return render(request,"project.html")
def skills(request):
    return render(request,"skills.html")