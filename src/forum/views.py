from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
    return render(request, 'forum.html', context)


def post_detail(request, pk):
    if request.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post=post)
        if request.method == "POST":
            author = request.POST.get('author', None)
            text = request.POST.get('text', None)
            post = request.POST.get('post', None)
            if author and text and post:
                comment = Comment.objects.create(
                    author=author, text=text, post=post)
        context = {
            'post': post,
            'comments': comments
        }
    return render(request, 'forum_detail.html', context)


def post_create(request):
    if request.is_authenticated:
        if request.method == "POST":
            title = request.POST.get('title', None)
            text = request.POST.get('text', None)
            if title and text:
                post = Post.objects.create(
                    author=request.user, title=title, text=text)
                return reverse("forum:detail", {kwargs:{'pk': post.pk}})
            return HttpResponse("Error")
        return HttpResponse('Post Creation')
    return HttpResponse("Error 404")
