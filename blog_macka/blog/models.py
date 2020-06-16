from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings


# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150, blank=True)
    pic = models.ImageField(upload_to='imgs/', blank=True)


class BlogEntry(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(default='',
                            editable=False,
                            max_length=250)
    author = models.ForeignKey('auth.User',
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pictures = models.ManyToManyField(Picture)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('blog:post_entry', kwargs=kwargs)
