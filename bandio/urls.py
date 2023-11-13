from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Maps the root URL to the 'home' view
    path('about/', views.about, name='about'),  # Maps the 'about/' URL to the 'about' view
    path('contact/', views.contact, name='contact'),  # Maps the 'contact/' URL to the 'contact' view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Uses Django's built-in LoginView
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),  # Uses Django's built-in LogoutView
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),  # Uses Django's built-in PasswordChangeView
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),  # Uses Django's built-in PasswordChangeDoneView
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),  # Uses Django's built-in PasswordResetView
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),  # Uses Django's built-in PasswordResetDoneView
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),  # Uses Django's built-in PasswordResetConfirmView
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),  # Uses Django's built-in PasswordResetCompleteView
    path('register/', views.registration, name='registration'),  # Maps the 'register/' URL to the 'registration' view for user registration
]
