import datetime
import random
from .models import BlogPost, Comment
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BlogPostForm

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
    comments = Comment.objects.filter(post_id=pk)
    return render(request, "blog_detail.html", context={"post": post, "comments": comments})

def create_comment(request, pk):
    if request.method == "POST":
        data: dict = request.POST
        post = BlogPost.objects.get(pk=pk)
        comment = Comment.objects.create(text=data["text"], post=post)
        return redirect(f'/blog/{pk}/')

#def add_post(request):
#    if request.method == "POST":

def test(request):
    error = ''
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            error = 'Форма была неверной'

    form = BlogPostForm()

    data ={
        'form': form,
        'error': error,
    }
    return render(request, "add_post.html", data)