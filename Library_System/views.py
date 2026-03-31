from django.shortcuts import render
from .models import Book
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'Library_System/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'Library_System/book_list.html', {'books':books})

def about(request):
    return render(request, 'Library_System/about_us.html')

def help(request):
    return render(request, 'Library_System/help.html')

def FAQ(request):
    return render(request, 'Library_System/FAQ.html')

def TaP(request):
    return render(request, 'Library_System/TaP.html')

def contact(request):
    return render(request, 'Library_System/contact.html')