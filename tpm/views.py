from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('This is Home Page')


def about(request):
    return HttpResponse('This is About page')


def dashboard(request):
    return render(request, 'dashboard.html')


def computer(request):
    return render(request, 'computer.html')


def electrical(request):
    return render(request, 'electrical.html')


def mechanical(request):
    return render(request, 'mechanical.html')


def biomedical(request):
    return render(request, 'biomedical.html')
