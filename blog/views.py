from django.shortcuts import render
from .models import Blog

def posts(request):
    posted = Blog.objects.all()
    return render(request, "blogpage.html",{"posts":posted})
# Create your views here.
def home(request):
    return render(request, "home.html")