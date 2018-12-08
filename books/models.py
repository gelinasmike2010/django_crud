from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime

currentYear = datetime.now().year

class Book(models.Model):
    book_title = models.CharField(max_length=300, unique=True)
    book_author = models.CharField(max_length=90, unique=True)
    book_year = models.IntegerField(validators = [MaxValueValidator(currentYear)])

    def __str__(self):
        return self.book_title

class Review(models.Model):
    # using Foreign Key creates a many-to-one relationship between Book and Review
        # i.e. one book can have many reviews
    book_title = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_review = models.CharField(max_length=750)

    def __str__(self):
        return self.book_title
