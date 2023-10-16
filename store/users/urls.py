# from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import UserLoginView, UserRegistrationView, ProfileUserView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', ProfileUserView.as_view(), name='profile')
]