from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all, name='all'),
    path('<int:chai_id>/', views.detail, name='detail'),
    
   
]