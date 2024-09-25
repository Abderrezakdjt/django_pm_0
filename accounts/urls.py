from django.contrib.auth.views import LoginView
from django.urls import path, include
from accounts.forms import UserLoginForm
from accounts.views import RegisterView, edit_profile, delete_account, change_password


urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
    path('delete-account/', delete_account, name='delete_account'),
    path('', include('django.contrib.auth.urls')),
    path('change-password/', change_password, name='change_password'),
]