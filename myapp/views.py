from django.shortcuts import render, HttpResponse
from .models import TodoModel

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoModel.objects.all()
    return render(request, "todo.html", {"todos": items})