from django.shortcuts import render

# Create your views here.

def Number_views(request):
    return render(request, 'Number/Number.html')

def No_views(request):
    return render(request, 'Number/Number Writing.html')

def Num_views(request):
    return render(request, 'Number/Number Word.html')