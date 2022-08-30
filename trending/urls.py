from django.urls import path
from . import views

urlpatterns = [
    path('panel/trending', views.trend_add, name='trend_add'),
    path('panel/trend_del/<int:pk>/', views.trend_del, name='trend_del'),
    path('panel/trend_edit/<int:pk>/', views.trend_edit, name='trend_edit'),
]

