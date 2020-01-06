from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Destination, Contact


def index(request):
    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        return HttpResponse("conact save in database")
        return redirect('/index')
    return render(request, 'contact.html')

