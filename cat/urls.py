from django.urls import path
from . import views

urlpatterns = [
    path('panel/cat_list', views.cat_list, name='cat_list'),
    path('panel/cat_add', views.cat_add, name='cat_add'),
    path('export/cat/csv', views.export_cat_csv, name='export_cat_csv'),
    path('import/cat/csv', views.import_add_csv, name='import_add_csv'),

]
