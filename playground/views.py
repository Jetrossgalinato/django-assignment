from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    # Your calculation logic here
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html')
