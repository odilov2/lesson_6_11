from django.urls import path
from .views import LandingPageView, CourseListView, TeacherListView

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing"),
    path("courses/", CourseListView.as_view(), name="courses"),
    path("teacher/", TeacherListView.as_view(), name="teacher"),
]
