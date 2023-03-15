from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    data={
        'title':'CRITICANIME'
    }
    return render(request,"minor.html",data)

def desc(request):
    return render(request,"desc-1.html")

def lat(request):
    return render(request,"lat-1.html")

def anime(request):

    return render(request,"anime.html")

def login(request):
    return render(request,"logIn.html")

def signup(request):
    return render(request,"signUp.html")