from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseNotFound
def successful(request):
    return HttpResponseNotFound("This is a custom 404 error page.",status=200)
def created(request):
    return HttpResponseNotFound("Created", status=201)
def accepted(request):
    return HttpResponseNotFound("Accepted", status=202)
def found(request):
    return HttpResponseNotFound("Found", status=302)
