from django.shortcuts import render
from django.views import View
from .models import Courses, Specialities, Teacher


class LandingPageView(View):
    def get(self, request):
        specialities = Specialities.objects.all()
        courses = Courses.objects.all()
        context = {
            "specialities": specialities,
            "courses": courses
        }
        return render(request, "landing.html", context)


class CourseListView(View):
    def get(self, request):
        courses = Courses.objects.all()
        context = {
            "courses": courses
        }
        return render(request, "courses.html", context)


class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            "teachers": teachers
        }
        return render(request, "teachers.html", context)
