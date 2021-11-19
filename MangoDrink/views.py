from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'MangoDrink/index.html')

def other(request):
    return render(request, 'MangoDrink/other.html')

def information(request):
    return render(request, 'MangoDrink/information.html')
