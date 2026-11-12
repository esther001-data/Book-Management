from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    year = models.IntegerField()
    cost = models.IntegerField()
    isbn = models.IntegerField(unique=True, max_length=15, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'book'

# python manage.py makemigrations
# python manage.py migrate


