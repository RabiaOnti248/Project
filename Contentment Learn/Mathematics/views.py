from django.shortcuts import render

# Create your views here.

def Mathematics_views(request):
    return render(request, 'Mathematics/Mathematics.html')

def Addition_views(request):
    return render(request, 'Mathematics/Addition.html')

def Subtraction_views(request):
    return render(request, 'Mathematics/Subtraction.html')

def Multiplication_views(request):
    return render(request, 'Mathematics/Multiplication.html')

def Division_views(request):
    return render(request, 'Mathematics/Division.html')

