from django.shortcuts import render, get_object_or_404, redirect
from .models import Trending
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage


def trend_add(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    trend_list = Trending.objects.all()

    if request.method == "POST":

        txt = request.POST.get('trend')

        if txt == "":
            error = "Field shouldn't be empty"
            return render(request, 'back/error.html', {'error': error})

        b = Trending(txt=txt)
        b.save()

    return render(request, 'back/trending.html', {'trend_list': trend_list})


def trend_del(request, pk):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    b = Trending.objects.filter(pk=pk)
    b.delete()

    return redirect('trend_add')


def trend_edit(request, pk):

    txt = Trending.objects.get(pk=pk).txt

    if request.method == "POST":

        txt = request.POST.get('trend')

        if txt == "":
            error = "Field shouldn't be empty"
            return render(request, 'back/error.html', {'error': error})

        b = Trending.objects.get(pk=pk)

        b.txt = txt
        b.save()
        return redirect('trend_add')

    return render(request, 'back/trend_edit.html', {'txt': txt, 'pk': pk})
