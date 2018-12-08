from django import forms
from books.models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_title', 'book_author', 'book_year',]
