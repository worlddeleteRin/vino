from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def index (request):
    template = 'main/base.html'
    context = {
	}
    return render(request, template, context)

def app_client (request):
    template = 'main/base.html'
    context = {}
    return render(request, template, context)

