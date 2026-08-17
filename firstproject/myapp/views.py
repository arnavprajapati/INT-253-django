from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("welcome to about page")

def contact(request):
    return HttpResponse("welcome to contact page")

def gallery(request):
    return HttpResponse("welcome to gallery page")