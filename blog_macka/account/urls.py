from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('register/', views.register, name='register'),
    # path('password_reset',
         # auth_views.PasswordResetView.as_view(),
         # name='password_reset'),
    path('', include('django.contrib.auth.urls')),
]
