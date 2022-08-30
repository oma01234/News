from django.urls import path
from . import views

urlpatterns = [
    path('comment/add/news/<pk>', views.news_cm_add, name='news_cm_add'),
    path('panel/comment/del/<int:pk>/', views.comment_del, name='comment_del'),
    path('panel/comment/confirm/<int:pk>/', views.comment_confirm, name='comment_confirm'),
    path('panel/comment_list', views.comment_list, name='comment_list'),

]
