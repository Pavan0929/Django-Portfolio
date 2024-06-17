from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('about/',views.about,name='about'),
]