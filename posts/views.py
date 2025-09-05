from django.shortcuts import render, HttpResponse
from posts.models import Post

def hello_view(request):
    return HttpResponse('Hello user!')

def html_view(request):
    return render(request, "test.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})

def details_view(request,):
    post = Post.objects.get(id=1)
    return render(request, "posts/post.html", context={"post": post})