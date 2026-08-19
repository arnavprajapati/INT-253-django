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

def items(request):
    item={
        'pie' : 'cost is 200',
        'ice cream' : 'cost is 600' 
    }
    content="<h1> items are </h1>"

    for item, cost in item.items():
        content += f"<li>{item}: {cost}</li>"
    
    return HttpResponse(content)

def students(request, marks):
    if marks >= 40:
        return HttpResponse(f"Student Passed! Marks: {marks}")
    else:
        return HttpResponse(f"Student Failed! Marks: {marks}")

def greet(request, name):
    return HttpResponse(f"greeting to {name}")