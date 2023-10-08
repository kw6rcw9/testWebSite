from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import News
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ShowNewsView(ListView):
    model = News
    template_name = 'main/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 2

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] =  'Главная страница сайта' 
        return ctx
    

class UserAllNewsView(ListView):
    model = News
    template_name = 'main/user_news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(autor=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)
        ctx['title'] =  'Главная страница сайта' 
        name = self.kwargs.get('username')
        ctx["title"] = f'Articles by {name}'

        return ctx
    
class NewsDetailView(DetailView):
    model = News
    template_name = 'main/news-detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx
    
class CreateNewsView(LoginRequiredMixin,CreateView):
    model = News
    template_name = 'main/create_news.html'
    fields = ['title', 'text']
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Add article'
        ctx['btn_text'] = 'Add article'
        return ctx

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'main/create_news.html'
    fields = ['title', 'text']
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Update article'
        ctx['btn_text'] = 'Update article'
        return ctx
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True
        return False


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'main/delete_news.html'
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True
        return False


def contacty(request):
    return render(request, 'main/contacty.html', {'title': 'Page'})