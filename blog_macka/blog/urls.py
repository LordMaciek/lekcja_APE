from django.urls import path
from . import views
from .views import PostEntry

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_pic/', views.create_pic, name='create_pic'),
    path('pic_list/', views.pic_list, name='pic_list'),
    # path('<int:pk>-<str:slug>/', views.post_entry, name='post_entry'),
    path('<int:pk>-<str:slug>/', PostEntry.as_view(), name='post_entry'),
]
