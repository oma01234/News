from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
from subcat.models import SubCat
import datetime
from cat.models import Cat
from trending.models import Trending
import random
from comment.models import Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def news_detail(request, word):

    site1 = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]

    shownews = News.objects.filter(name=word)
    tip = News.objects.filter(act=1).order_by('-show')
    tip2 = News.objects.filter(act=1).order_by('-show')[:2]

    tagname = News.objects.get(name=word).tag
    tag = tagname.split(',')
    trend = Trending.objects.all().order_by('-pk')

    # the dash - before "pk" helps arrange from latest to oldest

    try:

        mynews = News.objects.get(name=word)
        mynews.show = mynews.show + 1
        mynews.save()

    except:
        print("Can't add show")

    code = News.objects.get(name=word).pk
    comment = Comment.objects.filter(news_id=code, status=1).order_by('-pk')[:3]
    cmcount = len(comment)

    link = "/urls/" + str(News.objects.get(name=word).rand)

    return render(request, 'front/news_detail.html', {'trend': trend, 'site': site1, 'news': news, 'cat': cat, 'subcat': subcat,
                                                      'lastnews': lastnews, 'shownews': shownews, 'comment': comment, 'link': link,
                                                      'tip': tip, 'tip2': tip2, 'tag': tag, 'code': code, 'cmcount': cmcount})


def news_detail_short(request, pk, word):

    site1 = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]

    shownews = News.objects.filter(rand=pk)
    tip = News.objects.all().order_by('-show')
    tip2 = News.objects.all().order_by('-show')[:2]

    tagname = News.objects.get(rand=pk).tag
    tag = tagname.split(',')
    trend = Trending.objects.all().order_by('-pk')


    # the dash - before "pk" helps arrange from latest to oldest

    try:

        mynews = News.objects.get(rand=pk)
        mynews.show = mynews.show + 1
        mynews.save()

    except:
        print("Can't add show")

    link = "/urls/" + str(News.objects.get(name=word).rand)

    return render(request, 'front/news_detail.html', { 'trend': trend, 'site': site1, 'news': news, 'cat': cat, 'subcat': subcat,
                                                      'lastnews': lastnews, 'shownews': shownews, 'link': link,
                                                      'tip': tip, 'tip2': tip2, 'tag': tag})


def news_list(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        news = News.objects.filter(author=request.user)

    elif perm == 1:
        newss = News.objects.all()
        paginator = Paginator(newss, 2)
        page = request.GET.get('page')

        try:
            news = paginator.page(page)

        except EmptyPage:
            news = paginator.page(paginator.num_pages)

        except PageNotAnInteger:
            news = paginator.page(1)

    return render(request, 'back/news_list.html', {'news': news})


def news_edit(request, pk):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    if len(News.objects.filter(pk=pk)) == 0:
        error = 'News Not Found'
        return render(request, 'back/error.html', {'error': error})

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        a = News.objects.get(pk=pk).author
        if str(a) != str(request.user):
            error = "Sorry, You are not allowed to view this page"
            return render(request, 'back/error.html', {'error': error})

    cat = SubCat.objects.all()
    news = News.objects.get(pk=pk)
    date = datetime.datetime.now()
    # when using the get() method, there is no need for a for loop in the html file since it is specific already

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('Zimb')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('Zimb')
        tag = request.POST.get('tag')
        #  try using for google multi user authentication

        if newstitle == "" or newscat == "" or newstxtshort == "" or newstxt == "":
            error = 'All Fields Required'
            print(newscat)
            # for error to show in the html page, it needs to be placed in a dict {'error': error}
            return render(request, 'back/error.html', {'error': error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith('image'):

                if myfile.size < 5000000:

                    newsname = SubCat.objects.get(pk=newsid).name
                    print(newsname)

                    b = News.objects.get(pk=pk)

                    fss = FileSystemStorage()
                    fss.delete(b.picname)

                    b.name = newstitle
                    b.short_txt = newstxtshort
                    b.body_txt = newstxt
                    b.picname = filename
                    b.picurl = url
                    b.catname = newsname
                    b.catid = newsid
                    b.tag = tag
                    b.act = 0

                    b.save()

                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(myfile)

                    error = 'Your file Is Bigger Than 5Mb'
                    return render(request, 'back/error.html', {'error': error})
            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = 'Your file Is Not Supported'
                return render(request, 'back/error.html', {'error': error})

        except:

            newsname = SubCat.objects.get(pk=newsid).catname

            b = News.objects.get(pk=pk)

            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            b.catname = newsname
            b.catid = newsid
            b.date = date
            b.tag = tag

            b.save()
            
            return redirect('news_list')

    return render(request, 'back/news_edit.html', {'pk': pk, 'news': news, 'cat': cat})


def add_news(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    randint = str(random.randint(1000, 9999))
    rand = str(datetime.date.today().year) + str(randint)
    rand = int(rand)

    while len(News.objects.filter(rand=rand)) != 0:
        randint = str(random.randint(1000, 9999))
        rand = str(datetime.date.today().year) + str(randint)
        rand = int(rand)

    cat = SubCat.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('Zimb')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('Zimb')
        tag = request.POST.get('tag')
        #  try using for google multi user authentication

        if newstitle == "" or newscat == "" or newstxtshort == "" or newstxt == "":
            error = 'All Fields Required'
            print(newscat)
            # for error to show in the html page, it needs to be placed in a dict {'error': error}
            return render(request, 'back/error.html', {'error': error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith('image'):

                if myfile.size < 5000000:

                    newsname = SubCat.objects.get(pk=newsid).catname
                    ncatid = SubCat.objects.get(pk=newsid).catid
                    print(newsname)

                    b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, author=request.user, picname=filename,
                             picurl=url,
                             catname=newsname, catid=newsid, ncatid=ncatid, show=0, tag=tag, rand=rand)
                    b.save()

                    count = len(News.objects.filter(ncatid=ncatid))

                    b = Cat.objects.get(pk=ncatid)
                    b.count = count
                    b.save()

                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(myfile)

                    error = 'Your file Is Bigger Than 5Mb'
                    return render(request, 'back/error.html', {'error': error})
            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = 'Your file Is Not Supported'
                return render(request, 'back/error.html', {'error': error})

        except:
            error = 'INVALID'
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/add_news.html', {'cat': cat})


def news_delete(request, pk):

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

    try:
        b = News.objects.get(pk=pk)

        fs = FileSystemStorage()
        fs.delete(b.picname)

        ncatid = News.objects.get(pk=pk).ncatid

        b.delete()

        count = len(News.objects.filter(ncatid=ncatid))

        m = Cat.objects.get(pk=ncatid)
        m.count = count
        m.save()

    except:
        error = 'Something wrong'
        return render(request, 'back/error.html', {'error': error})

    return redirect('news_list')


def news_publish(request, pk):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    news = News.objects.get(pk=pk)
    news.act = 1
    news.save()

    return redirect('news_list')


def news_all_show(request, word):

    catid = Cat.objects.get(name=word).pk
    allnews = News.objects.filter(ncatid=catid)
    site1 = Main.objects.get(pk=1)
    site = Main.objects.filter(pk=1)
    cat = Cat.objects.all()
    news = News.objects.filter(act=1).order_by('-pk')
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    tip = News.objects.filter(act=1).order_by('-show')
    tip2 = News.objects.filter(act=1).order_by('-show')[:2]
    trend = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = News.objects.all().order_by('-pk')

    return render(request, 'front/all_news.html', {'site': site1, 'allnews': allnews, 'news': news,  'cat': cat, 'subcat': subcat, 'lastnews2': lastnews2,
                                               'lastnews': lastnews, 'tip': tip, 'tip2': tip2, 'trend': trend})

