# -*- coding:utf-8 -*-
from django.urls import path
from VideoLib import views

app_name = 'VideoLib'
urlpatterns = [
    path('test.py', views.test, name='test'),
]
