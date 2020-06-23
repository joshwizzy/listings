from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts import views
from accounts.views import RegistrationView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]