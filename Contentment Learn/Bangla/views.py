from django.shortcuts import render

# Create your views here.

def Bangla_views(request):
    return render(request, 'Bangla/Bangla.html')


def soroborno_views(request):
    return render(request, 'Bangla/স্বরবর্ণ অক্ষর.html')

def shoroborno_views(request):
    return render(request,'Bangla/স্বরবর্ণ শব্দ.html')

def banjonborno_views(request):
    return render(request,'Bangla/ব্যঞ্জনবর্ণ অক্ষর.html')

def benjonborno_views(request):
    return render(request,'Bangla/ব্যঞ্জনবর্ণ শব্দ.html')