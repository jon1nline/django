from django.urls import path
from . import views

urlpatterns = [
    path("",views.blogpage, name = "blogpage"),
    path("newpost",views.newpost, name = "newpost"),
    path('deletepost/<int:pk>/', views.deletepost, name='deletepost'),
]
