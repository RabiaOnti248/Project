"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from home.views import home_views
from Bangla.views import Bangla_views, soroborno_views, shoroborno_views, banjonborno_views, benjonborno_views
from signup.views import signup_views


from Education.views import Education_views
from English.views import English_views, Eng_views, En_views
from Number.views import Number_views, No_views, Num_views 
from Mathematics.views import Mathematics_views, Addition_views, Subtraction_views, Multiplication_views, Division_views
from Human.views import Human_views
from UserProfile.views import UserProfile_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_views, name='home'),
    path('home',home_views, name='home'),
    path('signin/',signup_views, name='signin'), 
    path('signout/',signup_views, name='signout'),

    path('UserProfile/',UserProfile_views, name='UserProfile'),
    path('Bangla/',Bangla_views, name='Bangla'),
    path('Education/',Education_views, name='Education'),
    path('English/',English_views, name='English'),
    path('Number/',Number_views, name='Number'),
    path('Mathematics/',Mathematics_views, name='Mathematics'),
   path('Human/',Human_views, name='Human'),
   path('soroborno/',soroborno_views, name='soroborno'),
   path('shoroborno/',shoroborno_views, name='shoroborno'),
   path('banjonborno/',banjonborno_views, name='banjonborno'),
   path('benjonborno/',benjonborno_views, name='benjonborno'),
   path('Eng/',Eng_views, name='Eng'),
   path('En/',En_views, name='En'),
   path('Addition/',Addition_views, name='Addition'),
   path('Subtraction/',Subtraction_views, name='Subtraction'),
   path('Multiplication/',Multiplication_views, name='Multiplication'),
   path('Division/',Division_views, name='Division'),
   path('No/',No_views, name='No'),
   path('Num/',Num_views, name='Num'),

]
