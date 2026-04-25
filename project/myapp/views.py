from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    data = {
        "city":"Odesa",
        "year":2026,
        "streets":["Sadovaya", "Novoselskogo", "Filatova"]
    }
    return render(request, 'home.html', data)

def contacts(request):
    return HttpResponse("Contacts")

def about(request, id):
    return HttpResponse(f'About {id}')