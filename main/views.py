from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
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

# Create your views here.


def home(request):

    site1 = Main.objects.get(pk=1)
    news = News.objects.filter(act=1).order_by('-pk')
    site = Main.objects.filter(pk=1)
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    tip = News.objects.filter(act=1).order_by('-show')
    tip2 = News.objects.filter(act=1).order_by('-show')[:2]
    trend = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = News.objects.all().order_by('-pk')

    # random_objects = Trending.objects.all()[randint(0, len(trend)-1)]
    # print(random_objects)

    #  Main.objects.all() is used to extract all the variables from the Main model in the database
    # while Main.objects.filter(pk=1) filters and selects a particular one

    # return render(request, 'front/home.html', {'site': site})
    return render(request, 'front/home.html', {'site': site1, 'news': news, 'cat': cat, 'subcat': subcat, 'lastnews2': lastnews2,
                                               'lastnews': lastnews, 'tip': tip, 'tip2': tip2, 'trend': trend})
# request here helps to ask for which page that is to be rendered


def web(request):
    return render(request, 'Webpage.html')


def panel(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')
    perm = 0
    perms = Permission.objects.filter(user=request.user)
    for i in perms:
        if i.codename == 'masteruser': perm = 1

    # test = ['i', '0', '#', 'h', 's']
    # # why does ["i", "0", "#", "h", "s"] not work for the random letters
    # rand = ""
    # for i in range(12):
    #     rand += random.choice(string.ascii_letters)
    #     rand += random.choice(test)

    # count = News.objects.count()
    # rand = News.objects.all()[random.randint(0, count - 1)]

    rand = 2869716746258

    return render(request, 'back/home.html', {'rand': rand})


def mylogin(request):

    if request.method == 'POST':

        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')

        if utxt != '' and ptxt != '':

            user = authenticate(username=utxt, password=ptxt)

            if user:
                login(request, user)
                return redirect('panel')

    return render(request, 'front/login.html')


def myregister(request):

    if request.method == "POST":

        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if name == "":
            msg = "Name field must be filled"
            return render(request, 'front/msgbox.html', {'msg': msg})

        print(uname, email, password1, password2)

        if password1 != password2:
            msg = "Your passwords didn't match"
            return render(request, 'front/msgbox.html', {'msg': msg})

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in password1:
            if '0' <= i <= '9':
                count1 = 1
            if 'A' <= i <= 'Z':
                count2 = 1
            if 'a' <= i <= 'z':
                count3 = 1
            if '!' <= i <= '(':
                count4 = 1

        if count1 == 0 or count2 == 0 or count3 == 0 or count4 == 0:
            msg = "Your password isn't strong enough"
            return render(request, 'front/msgbox.html', {'msg': msg})

        if len(password1) < 8:
            msg = "Your password is too short"
            return redirect(request, 'front/msgbox.html', {'msg': msg})

        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0:

            ip, is_routable = get_client_ip(request)

            if ip is None:
                ip = "0.0.0.0"

            try:
                response = DbIpCity.get(ip, api_key='free')
                country = response.country + " | " + response.city
            except:
                country = "Unknown"

            user = User.objects.create_user(username=name, email=email, password=password1)
            b = Manager(name=name, utxt=uname, email=email, ip=ip, country=country)
            b.save()

    return render(request, 'front/login.html')


def mylogout(request):

    logout(request)

    return redirect('mylogin')


def site_setting(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        error = "Sorry, You are not allowed to view this page"
        return render(request, 'back/error.html', {'error': error})

    if request.method == "POST":

        name = request.POST.get("name")
        tell = request.POST.get("tell")
        fb = request.POST.get("fb")
        tw = request.POST.get("tw")
        yt = request.POST.get("yt")
        link = request.POST.get("link")
        txt = request.POST.get("about")

        if fb == "": fb = "#"
        if tw == "": tw = "#"
        if yt == "": yt = "#"
        if link == "": link = "#"

        if name == "" or tell == "" or txt == "":
            error = "All fields required"
            return render(request, 'back/error.html', {'error': error})

        b = Main.objects.get(pk=1)

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            b.name = name
            b.tell = tell
            b.fb = fb
            b.tw = tw
            b.yt = yt
            b.link = link
            b.about = txt
            b.picurl = url
            b.picname = filename
            b.save()

        except:

            b.name = name
            b.tell = tell
            b.fb = fb
            b.tw = tw
            b.yt = yt
            b.link = link
            b.about = txt

            b.save()

    site = Main.objects.get(pk=1)

    return render(request, 'back/setting.html', {'site': site})


def about(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        error = "Sorry, You are not allowed to view this page"
        return render(request, 'back/error.html', {'error': error})

    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    tip = News.objects.all().order_by('-show')[:2]
    trend = Trending.objects.all().order_by('-pk')

    return render(request, 'front/about.html', {'site': site, 'news': news, 'cat': cat, 'subcat': subcat,
                                                'lastnews': lastnews, 'tip': tip, 'trend': trend})


def about_setting(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        error = "Sorry, You are not allowed to view this page"
        return render(request, 'back/error.html', {'error': error})

    if request.method == "POST":
        txt = request.POST.get('txt')
        
        if txt == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        b = Main.objects.get(pk=1)
        b.abouttxt = txt
        b.save()

    about = Main.objects.get(pk=1).abouttxt

    return render(request, 'back/about_setting.html', {'about': about})


def contact(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        error = "Sorry, You are not allowed to view this page"
        return render(request, 'back/error.html', {'error': error})

    site1 = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    tip = News.objects.all().order_by('-show')[:3]
    tip2 = News.objects.all().order_by('-show')[:2]
    trend = Trending.objects.all().order_by('-pk')

    return render(request, 'front/contact.html', {'site': site1, 'news': news, 'cat': cat, 'subcat': subcat,
                                               'lastnews': lastnews, 'tip': tip, 'tip2': tip2, 'trend': trend})


def change_password(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        error = "Sorry, You are not allowed to view this page"
        return render(request, 'back/error.html', {'error': error})

    if request.method == "POST":

        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 == "" or pass2 == "":
            error = "All fields Required"
            print(request.user)
            return render(request, 'back/error.html', {'error': error})

        user = authenticate(username=request.user, password=pass1)

        if user:
            if len(pass2) < 6:
                error = "Your password must be greater than six characters"
                return render(request, 'back/error.html', {'error': error})

            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0

            for i in pass2:
                if '0' <= i <= '9':
                    count1 = 1
                if 'A' <= i <= 'Z':
                    count2 = 1
                if 'a' <= i <= 'z':
                    count3 = 1
                if '!' <= i <= '(':
                    count4 = 1

            if count1 and count2 and count3 and count4 == 1:

                user = User.objects.get(username=request.user)
                user.set_password(pass2)
                user.save()
                return redirect('mylogout')


        else:
            error = "INCORRECT PASSWORD"
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/change_password.html')
