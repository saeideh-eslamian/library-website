from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.book_search, name='book_search'),
]