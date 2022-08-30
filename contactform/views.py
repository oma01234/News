from django.shortcuts import render, get_object_or_404, redirect
import datetime
from . models import ContactForm



def contact_add(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        txt = request.POST.get('msg')
        date = datetime.datetime.now()

        if name == "" or email == "" or txt == "":
            msg = 'All Fields Required'
            return render(request, 'front/msgbox.html', {'msg': msg})

        b = ContactForm(name=name, email=email, msg=txt, date=date)
        b.save()
        msg = "Your Message Received"
        return render(request, 'front/msgbox.html', {'msg': msg})

    return render(request, 'front/msgbox.html')


def contact_show(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    list = ContactForm.objects.all()

    return render(request, 'back/contact_form.html', {'list': list})


def contact_del(request, pk):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    b = ContactForm.objects.filter(pk=pk)
    b.delete()
    
    return redirect('contact_show')
