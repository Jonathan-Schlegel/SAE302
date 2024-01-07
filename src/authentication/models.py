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
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        """ Return string representation of our user """
        return self.email
