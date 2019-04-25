from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    my_dic = {
        "my_palabra": "hola",
        "my_numero": 123,
        "items": [1, 2, 3, 4]
    }
    return render(request, "home.html", my_dic)


def indice_view(request, *args, **kwargs):
    return render(request, "indice.html", {})
