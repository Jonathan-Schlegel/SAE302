from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from authentication.models import CustomUser

# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)  
        if user == None:    
            print("Le mot de passe est incorrect")
        else:
            login(request, user)
            match user.type:
                case "sender":
                    return redirect("/sender")
                case "transport":
                    return redirect("/transport")
                case "addressee":
                    print("check")
                    return redirect("/addressee")
    return render(request, 'authentication/html/login.html')

def log_out(request):
    logout(request)
    return redirect("/login")