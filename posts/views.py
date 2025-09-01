from django.shortcuts import render, HttpResponse

def hello_view(request):
    return HttpResponse('Hello user!')

def html_view(request):
    return render(request, "test.html")

