from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("welcome to about page")

def contact(request):
    message = "+91-1234567890"
    return HttpResponse(f"welcome to contact page {message}")

def gallery(request):
    return HttpResponse("welcome to gallery page ")