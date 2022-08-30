from django.urls import path
from . import views

urlpatterns = [
    path('panel/black_list', views.black_list, name='black_list'),
    path('panel/ip_add', views.ip_add, name='ip_add'),
    path('panel/ip/del/<int:pk>/', views.ip_del, name='ip_del'),
]
