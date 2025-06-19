from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='index'),
    path('search/', views.NewsSearchView.as_view(), name='search'),
    #path('api/news/', views.api_news_list, name='api_news_list'),
]