from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('api/hello/', views.api_hello, name='api_hello'),
]