from django.shortcuts import render

# Create your views here.

def signup_views(request):
    return render(request, 'signup/signin.html')

def home_views(request):
    return render(request, 'home/home.html')

def Bangla_views(request):
    return render(request, 'Bangla/Bangla.html')

def soroborno_views(request):
    return render('Bangla/স্বরবর্ণ অক্ষর.html')

def shoroborno_views(request):
    return render('Bangla/স্বরবর্ণ শব্দ.html')

def banjonborno_views(request):
    return render(request,'Bangla/ব্যঞ্জনবর্ণ অক্ষর.html')

def benjonborno_views(request):
    return render(request,'Bangla/ব্যঞ্জনবর্ণ শব্দ.html')

def Education_views(request):
    return render(request, 'Education/Education.html')

def English_views(request):
    return render(request, 'English/English.html')

def Number_views(request):
    return render(request, 'Number/Number.html')

def No_views(request):
    return render(request, 'Number/Number Writing.html')

def Num_views(request):
    return render(request, 'Number/Number Word.html')

def Mathematics_views(request):
    return render(request, 'Mathematics/Mathematics.html')

def Human_views(request):
    return render(request, 'Human/Human.html')

