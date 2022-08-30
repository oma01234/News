from django.urls import path
from . import views

urlpatterns = [
    path('news/<str:word>/', views.news_detail, name='news_detail'),
    path('panel/news_list', views.news_list, name='news_list'),
    path('panel/add_news', views.add_news, name='add_news'),
    path('panel/news_delete/<int:pk>/', views.news_delete, name='news_delete'),
    path('panel/news_edit/<int:pk>/', views.news_edit, name='news_edit'),
    path('panel/news_publish/<int:pk>/', views.news_publish, name='news_publish'),
    path('urls/<pk>/', views.news_detail_short, name='news_detail_short'),
    path('all/news/<str:word>', views.news_all_show, name='news_all_show'),

]
