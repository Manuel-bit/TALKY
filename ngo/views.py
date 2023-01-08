from django.shortcuts import render
from .models import *
# Create your views here.

def Index(request):
    return render(request, 'ngo/index.html')


def About(request):
    return render(request, 'ngo/about.html')


def memberRegister(request):
    return render(request, 'ngo/member_register.html')


def galery(request):
    title = 'Galery'
    galery_images = GaleryImage.objects.all()
    context = {
        'title':title,
        'galery_images':galery_images,
    }
    return render(request, 'ngo/galery.html', context)