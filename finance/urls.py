from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:name>/', views.index, name='index'),
    path('dashboard/<str:name>/delete/', views.delete_list, name='delete'),
]
