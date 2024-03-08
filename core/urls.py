from django.contrib import admin
from django.urls import path, include
from .views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('library.urls')),
    path('', LandingPageView.as_view(), name='landing'),
]
