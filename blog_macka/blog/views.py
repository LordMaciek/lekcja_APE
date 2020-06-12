from django.shortcuts import render, get_object_or_404
from .models import BlogEntry

# Create your views here.


def post_list(request):
    posts = BlogEntry.objects.all()
    return render(request,
                  'blog/list.html',
                  {'posts': posts})


def post_entry(request, post):
    post = get_object_or_404(BlogEntry,
                             slug=post)
    return render(request,
                  'blog/entry.html',
                  {'post': post})
