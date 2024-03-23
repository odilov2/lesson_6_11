from django.urls import path
from .views import (UserLoginView, UserRegisterView, UserListView, UserDetailView, UserSettingsView, LogOut,
UserDeleteView)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='users'),
    path('<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('users_delete/<int:id>/', UserDeleteView.as_view(), name='delete-user'),
    path('settings/<int:id>/', UserSettingsView.as_view(), name="settings"),
]
