from django.shortcuts import render, get_object_or_404
from blogapp.form import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
from blogapp.models import Blog


def home(request):
    blogs = Blog.objects.all()
    context = {
        "blogs":blogs
    }
    return render(request, "blogapp/index.html", context)


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, "blogapp/blog-posts.html", context)


def blogpost(request, slug, pk):
    form = CommentForm()
    # post = Blog.objects.get(pk=int(pk))
    post = get_object_or_404(Blog, pk=int(pk))
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.blog = post
            com.save()
            # return HttpResponseRedirect(reverse('blogapp:blogpost'))
    context = {
        'post':post
    }
    return render(request, 'blogapp/blog-post-details.html', context)
