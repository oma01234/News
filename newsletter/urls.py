from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/add/', views.newsletter, name='newsletter'),
    path('panel/newsletter/emails/', views.newsemail, name='newsemail'),
    path('panel/newsletter/phones/', views.newsphones, name='newsphones'),
    path('panel/newsletter/del/<int:pk>/<str:num>', views.news_txt_del, name='news_txt_del'),

]
