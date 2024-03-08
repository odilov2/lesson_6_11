from django.urls import path
from .views import UserLoginView, UserRegisterView, HomePageView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('home/', HomePageView.as_view(), name='home'),
]