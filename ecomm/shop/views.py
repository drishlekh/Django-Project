from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"shop/index.html")

def about(request):
    return HttpResponse("We are at about")
def contact(request):
    return HttpResponse("We are at contact")
def tracker(request):
    return HttpResponse("We are at tracker")
def search(request):
    return HttpResponse("We are at search")
def productview(request):
    return HttpResponse("We are at productview")
def checkout(request):
    return HttpResponse("We are at checkout")
# def home(request):
#     return render(request, 'home.html')