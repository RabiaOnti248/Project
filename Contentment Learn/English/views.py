from django.shortcuts import render

# Create your views here.

def English_views(request):
    return render(request, 'English/English.html')

def Eng_views(request):
    return render(request, 'English/English Alphabets.html')

def En_views(request):
    return render(request, 'English/English Word.html')