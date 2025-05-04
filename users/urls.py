from django.urls import path, include
from .views import Login, RegisterUser, Logout


urlpatterns = [
    path("login/", Login.as_view(),name="login"),
    path("register/", RegisterUser.as_view(),name="register"),
    path("logout/", Logout.as_view(), name="logout"),
]