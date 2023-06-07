from django.shortcuts import render

# Create your views here.

def Education_views(request):
    return render(request, 'Education/Education.html')
