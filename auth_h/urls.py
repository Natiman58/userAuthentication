from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('success/', views.success, name='success'),
    path('failure/', views.failure, name='failure'),
]