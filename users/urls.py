from django.urls import path
from .views import UserLoginView, UserRegisterView, HomePageView, UserListView, UserDetailView, UserSettingsView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('home/', HomePageView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='users'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('settings/<int:id>/', UserSettingsView.as_view(), name="settings"),
]