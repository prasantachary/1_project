from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def prasant(request):
    return HttpResponse('<h1><marquee>hi everyone</h1></marquee>')
