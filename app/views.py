from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def string_response(request):
    return HttpResponse('THIS IS MY FIRST STRING')

def second_response(request):
    return HttpResponse('THIS IS MY SECOND STRING')

def third_string(request):
    return HttpResponse('this is my third string')

def vasantha(request):
    return HttpResponse('THIS IS VASANTHA')

def chaithanya(request):
    return HttpResponse('one of my friend chaithanya')