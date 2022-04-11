from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="getroutes"),
    path('users-list/', views.getUsers, name="users"),
    path('user/<str:pk>/', views.getUser, name="users"),
]
