from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def blog(request):
    return render(request, 'pages/blog.html')


def singleBlog(request):
    return render(request, 'pages/single-blog.html')
