from django.shortcuts import render, HttpResponse, redirect
from posts.models import Post
from posts.forms import PostForm #PostForm2

def hello_view(request):
    return HttpResponse('Hello user!')

def html_view(request):
    return render(request, "test.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail_view.html", context={"post": post})

def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        # form = PostForm2()
        return render(request, 'posts/post_create.html', context={"form": form})
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        # form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        elif form.is_valid():
            # form.save()
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            image = form.cleaned_data.get("image")
        # # title = request.POST.get("title")
        # # content = request.POST.get("content")
        # # image = request.FILES.get("image")
        post = Post.objects.create(title=title, content=content, image=image)
        return redirect("/")