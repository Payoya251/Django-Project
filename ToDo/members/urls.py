from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('api/square-root/', views.calculate_square_root, name='calculate_square_root'),
]