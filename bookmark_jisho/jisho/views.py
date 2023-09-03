from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('test')

def search(request, query):
    return HttpResponse(f'query is {query}')