from django.shortcuts import render
from authentication.models import CustomUser

def sender(request):
    CustomUser.objects.create_user(email="test@test.fr", password="test", type="sender")
    return render(request, 'main/html/sender.html')

def transport(request):
    return render(request, 'main/html/transport.html')

def addressee(request):
    return render(request, 'main/html/addressee.html')

