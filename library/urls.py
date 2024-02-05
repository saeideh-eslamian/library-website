from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book/<slug:book_slug>/',views.book_detail, name='book_detail'),
    path('search/', views.book_search, name='book_search'),
    
]