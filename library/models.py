from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    count = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='library/authors/')

    def __str__(self):
        return f"{self.id} {self.title}"


class Customer(models.Model):
    Role = (('student', 's'),
            ('teacher', 't'))
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=Role, default='S')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.role}"


class BookRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    returned_date = models.DateField()
    create_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.customer} {self.book}"


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='library/images/')
    create_date = models.DateField(auto_now_add=True)
