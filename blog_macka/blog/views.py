from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from .models import BlogEntry, Picture
from .forms import CreateNewPost, PhotoAddForm

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

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['main_picture'] = ctx.get('object').pictures.all()[0]
        ctx['other_pix'] = ctx.get('object').pictures.all()[1:]
        return ctx

# def post_entry(request, post):
#     post = get_object_or_404(BlogEntry)
#     return render(request,
#                   'blog/entry.html',
#                   {'post': post})


def pic_list(request):
    pictures = Picture.objects.all()
    return render(request,
                  'blog/pic_list.html',
                  {'pictures': pictures})


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
            form.save_m2m()
            return redirect('blog:post_entry', pk=post.pk, slug=post.slug)
    else:
        form = CreateNewPost()
    return render(request, 'blog/create_post.html',
                  {'form': form,
                   })


@login_required
def create_pic(request):
    if request.method == 'POST':
        form = PhotoAddForm(data=request.POST,
                            files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'blog/create_pic.html',
                          {'form': form,
                           })
    else:
        form = PhotoAddForm()
    return render(request,
                  'blog/create_pic.html',
                  {'form': form,
                   })
