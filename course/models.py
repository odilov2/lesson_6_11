from django.db import models


class Specialities(models.Model):
    title = models.CharField(max_length=50)
    total_course = models.PositiveIntegerField()
    image = models.ImageField(upload_to="course/specialities/")

    def __str__(self):
        return self.title


class CourseRole(models.TextChoices):
    DRAFT = ("Ko'rinmasin", "Ko'rinmasin")
    Publish = ("Ko'rinsin", "ko'rinsin")


class Courses(models.Model):
    title = models.CharField(max_length=100)
    speciality = models.ManyToManyField(Specialities)
    image = models.ImageField(upload_to="course/course/")
    active_students = models.PositiveIntegerField(default=0)
    durection = models.PositiveIntegerField(default=0)
    price = models.FloatField()
    rayting = models.FloatField(default=0.0)
    status = models.CharField(max_length=20, choices=CourseRole.choices, default=CourseRole.Publish)
    create_date = models.DateField(auto_created=True)

    def __str__(self):
        return self.title


class Position(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Speciality = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="course/teacher")
    link_twitter = models.URLField(null=True, blank=True)
    link_facebook = models.URLField(null=True, blank=True)
    link_in = models.URLField(null=True, blank=True)
    create_date = models.DateField()

    def __str__(self):
        return self.first_name
