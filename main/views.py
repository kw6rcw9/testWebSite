from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Main page'
    }
    return render(request, 'main/home.html', data)
def contacty(request):
    return render(request, 'main/contacty.html', {'title': 'Page'})