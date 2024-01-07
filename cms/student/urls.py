from django.urls import path
from . import views

'''

The URL Patterns are just basics and are not containing any arguments to be passes to the view

'''
urlpatterns = [
    path('', views.Home, name='Home'),
    path('about/', views.About, name='About'),
    path('contact/', views.Contact, name='Contact'),
    path('add/', views.AddStudent, name='AddStudent'),
    path('edit/<int:id>/', views.EditStudent, name='Edit'),
    path('delete/<int:id>/', views.DeleteStudent, name='Delete'),
]
