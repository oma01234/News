from django.urls import path
from . import views

urlpatterns = [
    path('panel/manager/list/', views.manager_list, name='manager_list'),
    path('panel/manager/delete/<int:pk>/', views.manager_del, name='manager_del'),
    path('panel/manager/group/', views.manager_group, name='manager_group'),
    path('panel/manager/perms/', views.manager_perms, name='manager_perms'),
    path('panel/manager/group/add/', views.manager_group_add, name='manager_group_add'),
    path('panel/manager/group/delete/<str:name>/', views.manager_group_del, name='manager_group_del'),
    path('panel/manager/group/show/<int:pk>/', views.users_groups, name='users_groups'),
    path('panel/manager/addtogroup/<int:pk>/', views.add_users_groups, name='add_users_groups'),
    path('panel/manager/delgroup/<int:pk>/<str:name>/', views.del_users_groups, name='del_users_groups'),
    path('panel/manager/perms/add/', views.manager_perms_add, name='manager_perms_add'),
    path('panel/manager/perms/delete/<str:name>/', views.manager_perms_del, name='manager_perms_del'),
    path('panel/manager/perms/add/<int:pk>/', views.users_perms_add, name='users_perms_add'),
    path('panel/manager/perms/del/<int:pk>/<str:name>/', views.users_perms_del, name='users_perms_del'),
    path('panel/manager/perms/show/<int:pk>/', views.users_perms, name='users_perms'),
    path('panel/manager/addpermstogroup/<str:name>/', views.groups_perms, name='groups_perms'),
    path('panel/manager/del_perms_from_group/<str:name>/<str:gname>/', views.groups_perms_del, name='groups_perms_del'),
    path('panel/manager/add_perms_to_group/<str:name>', views.groups_perms_add, name='groups_perms_add'),

]
