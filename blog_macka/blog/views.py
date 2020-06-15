from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

from .models import BlogEntry
from .forms import CreateNewPost

# Create your views here.


def post_list(request):
    posts = BlogEntry.objects.all()
    return render(request,
                  'blog/list.html',
                  {'posts': posts})


class PostEntry(DetailView):
    model = BlogEntry
    query_pk_and_slug = True
    template_name = 'blog/entry.html'

# def post_entry(request, post):
#     post = get_object_or_404(BlogEntry)
#     return render(request,
#                   'blog/entry.html',
#                   {'post': post})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreateNewPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish = timezone.now()
            value = post.title
            post.slug = slugify(value, allow_unicode=False)
            post.save()
            return redirect('blog:post_entry', pk=post.pk, slug=post.slug)
    else:
        form = CreateNewPost()
    return render(request, 'blog/create_post.html',
                  {'form': form})
