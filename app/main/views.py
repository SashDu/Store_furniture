from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Welcome to',
        'list': ['first', 'second', 'third'],
        'dict': {'first': 1},
        'is_authenticated': False
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return HttpResponse("About page")