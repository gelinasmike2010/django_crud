from django.shortcuts import render

# import your models so that views can work with database
from books.models import Book, Review
from books.forms import BookForm

def home(request):
    # go to database, grab list of books and reviews, print in a table
    book_list = Book.objects.all()
    book_count = Book.objects.all().count()
    sum_of_years = 0
    for entry in Book.objects.all():
        sum_of_years += entry.book_year

    average_of_years = (sum_of_years / book_count)

# context is a dictionary of key-values
# call upon your variables by thir keys (within template tags) in templates
    context = {
        'book_count': book_count,
        'sum_of_years': sum_of_years,
        'book_list': book_list,
        'average_of_years': average_of_years,
    }

    return render(request, 'books/home.html', context=context)

def add_review(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = BookForm()
    return render(request, 'books/add_review.html', {'form': form})
