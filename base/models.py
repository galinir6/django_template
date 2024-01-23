from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    author = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['name','author']
 
    def __str__(self):
           return self.name + " - " + self.author