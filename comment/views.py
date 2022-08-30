from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from news.models import News
from manager.models import Manager
import datetime

# Create your views here.


def news_cm_add(request, pk):

    if request.method == 'POST':
        date = datetime.date.today()
        time_for = datetime.datetime.now()
        time = time_for.strftime("%H:%M:%S")

        cm = request.POST.get('msg')

        if request.user.is_authenticated:

            manager = Manager.objects.get(utxt=request.user)
            same_news = News.objects.get(pk=pk).name

            b = Comment(name=manager.name, email=manager.email, cm=cm,
                        news_id=pk, date=date, time=time, same_news=same_news)
            b.save()

        else:
            name = request.POST.get('name')
            email = request.POST.get('email')

            b = Comment(name=name, email=email, cm=cm, news_id=pk, date=date, time=time)
            b.save()

    newsname = News.objects.get(pk=pk).name

    return redirect('news_detail', word=newsname)


def comment_list(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        a = News.objects.get(pk=pk).author
        if str(a) != str(request.user):
            error = "Sorry, You are not allowed to view this page"
            return render(request, 'back/error.html', {'error': error})

    comment = Comment.objects.all()

    return render(request, 'back/comment_list.html', {'comment': comment})


def comment_del(request, pk):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    b = Comment.objects.filter(pk=pk)
    b.delete()

    return redirect('comment_list')


def comment_confirm(request, pk):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    b = Comment.objects.get(pk=pk)
    b.status = 1
    b.save()

    return redirect('comment_list')
