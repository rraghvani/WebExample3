from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.devices, name='devices'),
    path('toggle/<int:device_id>/', views.toggle_device, name='toggle_device'),
    path('favicon.ico', lambda request: redirect('/static/favicon.ico')),
    path('test/', views.test, name='test'),
    path('test/<int:device_id>/', views.toggle_test, name='toggle_test'),
]
