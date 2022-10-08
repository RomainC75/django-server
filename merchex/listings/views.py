from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello JD</h1>')

def about(request):
    return HttpResponse('<h1>About us page</h1>')

def data(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',
        {
            'band0': bands[0],
            'band1': bands[1],
            'band2': bands[2],
            'bands':bands,
            'length':len(bands)
        })


