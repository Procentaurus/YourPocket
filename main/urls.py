from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('settings/<int:pk>/', views.settings, name='settings'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('reset_password', auth_views.PasswordResetView.as_view(
        template_name='main/password_reset.html'),
        name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(
        template_name='main/password_reset_sent.html'),
        name='reset_password_sent'),
    path('reset_password_confirm', auth_views.PasswordResetConfirmView.as_view(
        template_name='main/password_reset_confirm.html'),
        name='reset_password_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='main/password_rese_complete.html'),
        name='reset_password_complete'),
]
