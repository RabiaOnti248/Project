from django.shortcuts import render

# Create your views here.

def Human_views(request):
    return render(request, 'Human/Human.html')