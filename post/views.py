import datetime
import random
from .models import BlogPost
from django.shortcuts import render
from django.http import HttpResponse

def hello_world_view(request):
    return HttpResponse("Hello, World!")

def date_view(request):
    now = datetime.datetime.now()
    return HttpResponse(str(now))

def random_view(request):
    ran = random.randint(0, 100)
    return HttpResponse(str(ran))

def blog_view(request):
    posts: list = BlogPost.objects.all()
    return render(request, "blog.html", context={"posts": posts})

def post_detail(request, pk):
    post: BlogPost = BlogPost.objects.get(pk=pk)
    return render(request, "blog_detail.html", context={"post": post})