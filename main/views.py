from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index (request):
    template = 'main/base.html'
    context = {}
    return render(request, template, context)
