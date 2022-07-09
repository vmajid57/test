from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('expense/', views.add_expence),
    path('thanks/', views.thanks),

]