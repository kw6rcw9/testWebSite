from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.ShowNewsView.as_view(), name='home'),
    path('news/add', views.CreateNewsView.as_view(), name='newsadd'),
    path('contacts', views.contacty, name='contacts'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete')

]
