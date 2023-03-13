from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bookcreate(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    book_name=models.CharField(max_length=600)
    issue_date=models.DateField()
    
    def __str__(self):
        return self.book_name
    
class book(models.Model):
    bookname=models.CharField(max_length=500)
class ubook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booklist=models.ForeignKey(book,on_delete=models.CASCADE)
class issuebook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booklist=models.ForeignKey(book,on_delete=models.CASCADE)
    issue_date=models.DateField()
class returnbook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booklist=models.ForeignKey(book,on_delete=models.CASCADE)
    return_date=models.DateField()
class Bookcreatedata(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    book_name=models.CharField(max_length=600)
    issue_date=models.DateField()
    
    def __str__(self):
        return self.book_name