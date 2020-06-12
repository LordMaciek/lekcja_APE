from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:post>/', views.post_entry, name='post_entry')
]
