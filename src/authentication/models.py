from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
            """ Create a new user profile """
            if not email:
                raise ValueError('User must have an email address')

            email = self.normalize_email(email)
            user = self.model(email=email)

            user.set_password(password)
            user.save()

            return user

    def create_superuser(self, email, password):
        """ Create a new superuser profile """
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    type = models.CharField(max_length=12, default="Null")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        """ Return string representation of our user """
        return self.email
    

class Sender(models.Model):
    name = models.CharField(max_length=30)
    id_package = models.ForeignKey("Package", on_delete=models.CASCADE)


class Vehicle(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    delivery = models.IntegerField()
	

class Transport(models.Model):
    name = models.CharField(max_length=30)
    id_package = models.ForeignKey("Package", on_delete=models.CASCADE)

    
class Addressee(models.Model):
    firstName = models.CharField(max_length=30)
    surName = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    mail = models.EmailField()
    phone = models.CharField(max_length=30)
    id_package = models.ForeignKey("Package", on_delete=models.CASCADE)


class Package(models.Model):
    weight = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
	

class State(models.Model):
    packaged = models.IntegerField()
    arrived = models.IntegerField()
    departed = models.IntegerField()
    delivered = models.IntegerField()
    received = models.IntegerField()
    id_package = models.ForeignKey("Package", on_delete=models.CASCADE)
    
    
class Location(models.Model):
    longitude = models.IntegerField()
    id_package = models.ForeignKey("Package", on_delete=models.CASCADE)
