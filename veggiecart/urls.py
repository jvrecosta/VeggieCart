from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('homepage',views.homepage,name='homepage'),
    path('signout',views.signout,name='signout'),
    path('google_login',views.google_login,name='google_login')
]
