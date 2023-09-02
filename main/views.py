from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h3> Hello world! </h3>')
def contacty(request):
     return HttpResponse('<h3> Contacts</h3>')