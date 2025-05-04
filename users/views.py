from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .forms import RegisterUserForm
from django.contrib.auth import login

# Create your views here.
class Login(LoginView):
    template_name = "users/account/login.html"

class Logout(LogoutView):
    next_page = "/"


class RegisterUser(FormView):
    template_name = "users/account/register.html"
    form_class = RegisterUserForm
    success_url = "/"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)