from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from . import forms


# Create your views here.
def post_list(request):
    """View function for home page of site."""
    posts = Post.objects.all().order_by("-date")
    return render(request, "posts/posts_list.html", {"posts": posts})


def post_page(request, slug):
    """View function for post page of site."""
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_page.html", {"post": post})


@login_required(login_url="/users/login/")
def post_new(request):
    """new post"""
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect("posts:list")
    form = forms.CreatePost()
    return render(request, "posts/post_new.html", {"form": form})
