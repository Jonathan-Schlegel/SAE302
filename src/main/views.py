from django.shortcuts import render
from authentication.models import CustomUser
from .models import Addressee, Package, Transport, Sender, Packaged, Arrived, Departure, Delivered, Received
from django.contrib.auth.decorators import login_required
import logging.config

@login_required(login_url='/login')
def sender(request):
    if request.method == "POST":
            match request.POST.get('id'):
                case "add-package":
                    transport = request.POST.get('transport')
                    addressee = request.POST.get('addressee')
                    weight = request.POST.get('weight')
                    length = request.POST.get('length')
                    width = request.POST.get('width')
                    height = request.POST.get('height')
                    latitude = request.POST.get('latitude')
                    longitude = request.POST.get('longitude')
                    sender_instance = Sender.objects.get(user_id=request.user.pk)

                    try:
                        transport_instance = Transport.objects.get(name=transport)
                        print(transport_instance)
                    except Transport.DoesNotExist:
                        print("Erreur lors de la récupération du transporteur")
                    try: 
                        addressee_instance = Addressee.objects.get(name=addressee)
                        print(addressee_instance)
                    except Addressee.DoesNotExist:
                        print("Erreur lors de la récupération du destinataire")
                    try:
                        package = Package.objects.create(weight=weight, length=length, width=width, height=height, sender=sender_instance, 
                                           transport=transport_instance, addressee=addressee_instance)
                        Packaged.objects.create(package=package, latitude=latitude, longitude=longitude)
                        Arrived.objects.create(package=package, latitude=latitude, longitude=longitude)
                        Departure.objects.create(package=package, latitude=latitude, longitude=longitude)
                        Delivered.objects.create(package=package, latitude=latitude, longitude=longitude)
                        Received.objects.create(package=package, latitude=latitude, longitude=longitude)

                    except:
                        print("Erreur lors de la création du colis")
                        pass

                case "add-transport":
                    transport = request.POST.get('transport')
                    email = request.POST.get('email')
                    password = request.POST.get('password')
                    try:
                        CustomUser.objects.get(email=email)
                    except CustomUser.DoesNotExist:
                        user = CustomUser.objects.create_user(email=email, password=password)
                        Transport.objects.create(name=transport, user=user)

                case "add-addressee":
                    name = request.POST.get('name')
                    address = request.POST.get('address')
                    postal_code = request.POST.get('postal_code')
                    city = request.POST.get('city')
                    phone = request.POST.get('phone')
                    email = request.POST.get('email')
                    password = request.POST.get('password')
                    try:
                        CustomUser.objects.get(email=email)
                    except CustomUser.DoesNotExist:
                        user = CustomUser.objects.create_user(email=email, password=password)
                        Addressee.objects.create(name=name, address=address, postal_code=postal_code, city=city, phone=phone, user=user)

    return render(request, 'main/html/sender.html')

@login_required(login_url='/login')
def transport(request):
    print("transport")
    return render(request, 'main/html/transport.html')

@login_required(login_url='/login')
def addressee(request):
    print("addressee")
    return render(request, 'main/html/addressee.html')
