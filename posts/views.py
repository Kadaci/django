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

def details_view2(request,):
    post2 = Post.objects.get(id=2)
    return render(request, "posts/post2.html", context={"post": post2})
    
def details_view3(request,):
    post3 = Post.objects.get(id=3)
    return render(request, "posts/post3.html", context={"post": post3}) 

def details_view4(request,):
    post4 = Post.objects.get(id=4)
    return render(request, "posts/post2.html", context={"post": post4})