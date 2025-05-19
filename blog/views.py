from django.shortcuts import render, redirect
from .models import Blog
from users.models import CustomUser
import datetime

def blogpage(request):
    posted = Blog.objects.filter(active=True)
    return render(request, "blogpage.html",{"posts":posted})
# Create your views here.
def home(request):
    return render(request, "home.html")

def newpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        datepost = datetime.date.today()
        user = CustomUser.objects.get(id=1)
        Blog.objects.create(title=title, message=content, date=datepost, idEscritor=user)  # save new posts to database
        return redirect('blogpage')  # Redirect to the main page
    return render(request, "createpost.html")

def deletepost(request):
    return redirect(blogpage)