from django.contrib import admin
from .models import Main
# Register your models here.
# 1 to use groups from django admin, we import "Permission"
from django.contrib.auth.models import Permission

admin.site.register(Main)
# 2 then we write >
admin.site.register(Permission)
