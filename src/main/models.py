from django.db import models
from authentication.models import CustomUser

class Sender(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)


class Transport(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)


class Vehicle(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    delivery = models.IntegerField()


class Addressee(models.Model):
    name = models.CharField(max_length=60, default=True)
    address = models.CharField(max_length=100, default=True)
    postal_code = models.IntegerField(default=True)
    city = models.CharField(max_length=30, default=True)
    phone = models.IntegerField()
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)


class Package(models.Model):
    weight = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    addressee = models.ForeignKey(Addressee, on_delete=models.CASCADE)

    
class Packaged(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Arrived(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Departure(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Delivered(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Received(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()