from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return HttpResponse(posts)
    return HttpResponse("Index")


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
                return HttpResponse("Comment Created")
            return HttpResponse("Error")
        context = {
            'post': post,
            'comments': comments
        }
        return HttpResponse({'post': post, 'comments': comments})
    return HttpResponse("Error 404")


def post_create(request):
    if request.is_authenticated:
        if request.method == "POST":
            title = request.POST.get('title', None)
            text = request.POST.get('text', None)
            if title and text:
                post = Post.objects.create(
                    author=request.user, title=title, text=text)
                return HttpResponse("Post Created")
            return HttpResponse("Error")
        return HttpResponse('Post Creation')
    return HttpResponse("Error 404")
