from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    # if request.user.is_authenticated:
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'forum.html', context)


def post_detail(request, pk):
    print(request.user)
    # if request.user.is_authenticated:
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments
    }
    print(comments)
    if request.method == "POST":
        text = request.POST.get('text', None)
        if text and post:
            comment = Comment.objects.create(
                author=request.user, text=text, post=post)
            return render(request, 'forum_detail.html', context)
        return render(request, 'forum_detail.html', context)
    return render(request, 'forum_detail.html', context)
    # return redirect('accounts:login')
    # return HttpResponse("Invalid")


def post_create(request, *args, **kwargs):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST.get('title', None)
            text = request.POST.get('text', None)
            if title and text:
                post = Post.objects.create(
                    author=request.user, title=title, text=text)
                return redirect('forum:detail', pk=post.pk)
            return render(request, 'forum_create.html')
        return render(request, 'forum_create.html')
    return HttpResponse("Error 404")
