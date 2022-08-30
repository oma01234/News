from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('webpage/', views.web, name='Webpage'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='About'),
    path('panel/', views.panel, name='panel'),
    path('panel/setting/', views.site_setting, name='site_setting'),
    path('panel/about/setting/', views.about_setting, name='about_setting'),
    path('login/', views.mylogin, name='mylogin'),
    path('register/', views.myregister, name='myregister'),
    path('logout/', views.mylogout, name='mylogout'),
    path('panel/change_password/', views.change_password, name='change_password'),

]
