from django.contrib import admin
from .models import Courses, Specialities, Teacher, Position


@admin.register(Specialities)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("title", "total_course")


@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "active_students", "durection", "price", "rayting", "status", "create_date")


@admin.register(Position)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "image", "link_twitter", "link_facebook", "link_in", "create_date")