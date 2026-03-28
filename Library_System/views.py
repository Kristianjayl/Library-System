from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'Library_System/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'Library_System/book_list.html', {'books':books})