from django.db import models

#Primary key est automatiquement créer si pas déclarer

class Sender(models.Model):
    name = models.CharField(max_length=30)

class Vehicle(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    delivery = models.IntegerField()
	
class Transport(models.Model):
    name = models.CharField(max_length=30)
    
class Addressee(models.Model):
    firstName = models.CharField(max_length=30)
    surName = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    mail = models.EmailField()
    phone = models.CharField(max_length=30)

class Package(models.Model):
    weight = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    senderID = models.ForeignKey(Sender, on_delete=models.CASCADE, null=True)
    transportID = models.ForeignKey(Transport, on_delete=models.CASCADE, null=True)
    addresseeID = models.ForeignKey(Addressee, on_delete=models.CASCADE, null=True)
    vehicleID = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
	
class State(models.Model):
    packaged = models.IntegerField()
    arrived = models.IntegerField()
    departed = models.IntegerField()
    delivered = models.IntegerField()
    received = models.IntegerField()
    packageID = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)

    
class Location(models.Model):
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    time = models.IntegerField()
    packageID = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)