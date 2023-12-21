from django.shortcuts import render
from authentication.models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def sender(request):
    return render(request, 'main/html/sender.html')

@login_required(login_url='/login')
def transport(request):
    return render(request, 'main/html/transport.html')

@login_required(login_url='/login')
def addressee(request):
    return render(request, 'main/html/addressee.html')

