from django.urls import path
from . import views

urlpatterns = [
    path('panel/subcat_add', views.subcat_add, name='subcat_add'),
    path('panel/subcat_list', views.subcat_list, name='subcat_list'),
]
