from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id} {self.title}"
