from django.db import models
from django.utils.html import escape#for image on Admin page


# Create your models here.


class Comments(models.Model):# I'm not sure about this being it's own class
    text=  models.TextField(null=True)
    def __str__(self):#shows values on Admin page
       return self.text
    

class User(models.Model):
    name =  models.CharField(max_length=50)
    comments = models.ForeignKey('Comments', on_delete=models.CASCADE, null=True)
    

class Author(models.Model):
    name =  models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):#shows values on Admin page
        return self.name

class Book(models.Model):
    image = models.ImageField(upload_to='staticImages')
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books') #Author needs to be foreing key: ForeingKey? Tied to Author's biography
    rating = models.IntegerField(null=True) #Static variable as a counter
    genre = models.CharField(max_length=50)
    topSeller = models.BooleanField(null=True) #based on a count of rating being >n?
    price = models.DecimalField(max_digits=5, decimal_places=2)
    releaseDate = models.DateTimeField()
    publisher = models.CharField(max_length=50)
    description = models.TextField() #Book Details App only
    #comments = models.ForeignKey('Comments',  on_delete=models.CASCADE,null=True)
    #comments = models.TextField()

    def __str__(self):#shows values on Admin page
        return self.title