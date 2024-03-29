# Generated by Django 5.0.3 on 2024-03-22 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('total_course', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='course/specialities/')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='course/course/')),
                ('active_students', models.PositiveIntegerField(default=0)),
                ('durection', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField()),
                ('rayting', models.FloatField(default=0.0)),
                ('status', models.CharField(choices=[("Ko'rinmasin", "Ko'rinmasin"), ("Ko'rinsin", "ko'rinsin")], default="Ko'rinsin", max_length=20)),
                ('speciality', models.ManyToManyField(to='course.specialities')),
            ],
        ),
    ]
