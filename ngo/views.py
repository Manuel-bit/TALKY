from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'ngo/index.html')

def About(request):
    return render(request, 'ngo/about.html')

def memberRegister(request):
    return render(request, 'ngo/member_register.html')