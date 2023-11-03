from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Hi on the women page here!')


def ids(request, womenid):
    if(request.GET):
        print('request.GET: ', request.GET)
    return HttpResponse(f'Id: {womenid}')

def pageNotFound(request, exception):
    return HttpResponseNotFound('Page not found')