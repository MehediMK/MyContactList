from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactList(models.Model):
    manager = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=30,blank=False)
    email = models.EmailField(max_length=50,blank=True,unique=True)
    phone = models.CharField(max_length=10,blank=False,unique=True)
    gender = models.CharField(max_length=6,default='select',choices=(('select','Select'),('male','Male'),('female','Female')),blank=False)
    cimg = models.ImageField(upload_to='images',blank=True)
    cinfo = models.CharField(max_length=15,blank=False)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
