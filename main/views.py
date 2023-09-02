from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    news = [
        {
            'title': 'Our first article',
            'text': 'full text',
            'date': '1 January 2100',
            


        },
        {
            'title': 'Our second article',
            'text': 'full text',
            'autor': 'John',
            'date': '10 January 2100',
            


        }
    ]
   
    data = {
        'news': news,
        'title': 'Main page'
    }
    return render(request, 'main/home.html', data)
def contacty(request):
    return render(request, 'main/contacty.html', {'title': 'Page'})