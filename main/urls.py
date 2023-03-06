from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('settings/<int:pk>/', views.settings, name='settings'),
    path('profile_data_visualisation/', views.profileDataVisualisation, name="profile_data_visualisation"),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('contact/', views.contact, name='contact'),

    path('add_income/', views.addIncome, name='add_income'),
    path('add_expense/', views.addExpense, name='add_expense'),
    path('confirm/<int:pk>/<str:type>/', views.confirm, name='confirm'),
    path('delete/<str:type>/<int:pk>/', views.deleteObject, name='delete'),
    path('edit/<str:type>/<int:pk>/', views.editObject, name='edit'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='main/password_reset.html'),
        name='password_reset'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='main/password_reset_sent.html'),
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='main/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='main/password_reset_complete.html'),
        name='password_reset_complete'),
]
