from django.shortcuts import render
from myapp1.models import Book
# Create your views here.
def show_book(request):
    books = Book.objects.all() #select * from books

    return render(request, 'show_book.html', {'books':books})


def add_book(request):
    Book.objects.create(title='Blossoms Of The Savannah',
                        year=2021,
                        category='Fiction',
                        cost=500,
                        isbn='745638744324',
                        published='True')
    Book.objects.create(title='Man Of The People',
                        year=2019,
                        category='Politics',
                        cost=550,
                        isbn='985664564324',
                        publisher='True')
    return render(request, 'add_book.html')