from django.urls import path
from . import views 
'''importing from the current directory'''
urlpatterns =[
    path('',views.home,name='front-home'),
  
    path('about/',views.about,name='front-about'),

    path('homepage/',views.hp,name='front-homepage'),
]