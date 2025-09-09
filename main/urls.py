from django.urls import path
from main.views import show_main

appname='main'

urlpatterns = [
    path('', show_main, name='show_main'),
]