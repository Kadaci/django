from django.shortcuts import render, HttpResponse, redirect
from posts.models import Post
from posts.forms import PostForm, PostForm2, SearchForm  
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def hello_view(request):
    return HttpResponse('Hello user!')

def html_view(request):
    return render(request, "test.html")

@login_required(login_url="/login/")
def post_list_view(request):
    posts = Post.objects.all()
    limit = 4
    if request.method == "GET":
        search = request.GET.get("search")
        category_id = request.GET.get("category_id")
        ordering = request.GET.get("ordering")
        page = int(request.GET.get("page", 1))
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if category_id:
            posts = posts.filter(category_id=category_id)
        if ordering:
            posts = posts.order_by(ordering)
        if page:
            max_pages = posts.count() / limit
            if round(max_pages) < max_pages:
                max_pages = round(max_pages) + 1
            elif round(max_pages) > max_pages:
                max_pages = round(max_pages)
            start = (page - 1) * limit
            end = page * limit
            posts = posts[start:end]

        form = SearchForm()
        return render(
            request, 
            "posts/post_list.html", 
            context={"posts": posts, "form": form}
        )

@login_required(login_url="/login/")
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail_view.html", context={"post": post })


@login_required(login_url="/login/")
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