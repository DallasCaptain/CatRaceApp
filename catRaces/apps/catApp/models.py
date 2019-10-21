from django.db import models
from datetime import date

# Create your models here.
class UserManager(models.Manager):
    def validate(self, formData):
        errors = []
        if formData['password'] != formData['confPass']:
            errors.append("password doesn't match")
        if len(formData['name']) < 2:
            errors.append('name to short')
        return errors



class User(models.Model):
    uname = models.CharField(max_length=128)
    bday = models.DateField(default = date.today() )
    password = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()




class Cat(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, related_name="cats", on_delete="CASCADE")
    likes = models.ManyToManyField(User,related_name='catsLiked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CatRace(models.Model):
    name = models.CharField(max_length=128)
    racers = models.ManyToManyField(Cat,related_name='races')
    winner = models.ForeignKey(Cat,related_name='wins',on_delete="CASCADE",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)