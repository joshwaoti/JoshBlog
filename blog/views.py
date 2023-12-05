from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post, Comment

def blog(request, post_id=None):
    categories = Category.objects.all()
    posts = Post.objects.all()[:5]
    single_post = None
    if post_id:
        single_post = get_object_or_404(Post, post_id=post_id)
    context = {
        "categories" : categories,
        "posts" : posts,
        "single_post" : single_post,
    }

    return render(request, "blog/category.html", context)

def singlePost(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    
    return render(request, "blog/single-post.html")