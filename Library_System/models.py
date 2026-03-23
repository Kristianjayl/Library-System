from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=40)
    genre = models.CharField(max_length=60)
    published_year =models.IntegerField()
    isbn = models.CharField(max_length=50)
    copies_total = models.IntegerField()

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    address = models.CharField(max_length=200)
    join_date = models.DateField(auto_now_add=True)

    def __str__ (self):
        return self.name

class Loan(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)#This is a Foreign Key
    member = models.ForeignKey(Member,on_delete=models.CASCADE)#This one too
    borrow_date =models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null = True, blank = True)

    def __str__ (self):
        return f"{self.book} borrowed by {self.member}"