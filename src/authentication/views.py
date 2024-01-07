from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from authentication.models import CustomUser
from main.models import Addressee, Transport, Sender
import logging

logger = logging.getLogger(__file__)

# Create your views here.
def log_in(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user == None:
            print("Le mot de passe est incorrect")
            return render(request, 'authentication/html/login.html')
        else:
            login(request, user)
            try:
                sender = Sender.objects.get(user_id=user.pk)
            except Sender.DoesNotExist: 
                sender = None
            try:
                transport = Transport.objects.get(user_id=user.pk)
            except Transport.DoesNotExist:
                transport = None
            try:
                addressee = Addressee.objects.get(user_id=user.pk)
            except Addressee.DoesNotExist:
                addressee = None
            if sender:
                logger.info(f"L'utilisateur {request.user} s'est connecté.")
                return redirect("sender")
            elif transport:
                logger.info(f"L'utilisateur {request.user} s'est connecté.")
                return redirect("transport")
            elif addressee:
                logger.info(f"L'utilisateur {request.user} s'est connecté.")
                return redirect("addressee")
    return render(request, 'authentication/html/login.html')   

def log_out(request):
    logout(request)
    return redirect("login")