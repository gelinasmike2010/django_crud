from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_review/', views.add_review, name='add_review'),
]
