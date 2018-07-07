from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request,"post/post.html")

def post(request):
    Post.objects.create(post=request.POST['post_area'])
    posts = Post.objects.all
    return render(request,"post/all.html", {"posts": posts})