from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsLetter
from main.models import Main
from django.core.files.storage import FileSystemStorage


def newsletter(request):

    if request.method == "POST":

        txt = request.POST.get('text')

        res = txt.find('@')
        
        if int(res) != -1:
            b = NewsLetter(txt=txt, status=1)
            b.save()
        else:
            try:
                int(txt)
                b = NewsLetter(txt=txt, status=2)
                b.save()
            except:
                return redirect('home')

    return redirect('home')


def newsemail(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    emails = NewsLetter.objects.filter(status=1)

    return render(request, 'back/emails.html', {'emails': emails})


def newsphones(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    phones = NewsLetter.objects.filter(status=2)

    return render(request, 'back/phones.html', {'phones': phones})


def news_txt_del(request, pk, num):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    b = NewsLetter.objects.get(pk=pk)
    b.delete()

    if int(num) == 2:
        return redirect('newsphones')

    return redirect('newsemails')
