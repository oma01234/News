from django.shortcuts import render, get_object_or_404, redirect
from .models import BlackList
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager
import random
import string
from random import randint
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity


def black_list(request):

    ip = BlackList.objects.all()

    return render(request, 'back/blacklist.html', {'ip': ip})


def ip_add(request):

    if request.method == "POST":

        ip = request.POST.get('ip')

        if ip != "":
            b = BlackList(ip=ip)
            b.save()

    return redirect('black_list')


def ip_del(request, pk):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        error = "Sorry, You are not allowed to view this page"
        return render(request, 'back/error.html', {'error': error})
    if not request.user.is_authenticated:
        return redirect('mylogin')

    ip = BlackList.objects.get(pk=pk)
    ip.delete()

    return redirect('black_list')
