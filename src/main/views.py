from django.shortcuts import render

def sender(request):
    return render(request, 'main/html/sender.html')

def transport(request):
    return render(request, 'main/html/transport.html')

def addressee(request):
    return render(request, 'main/html/addressee.html')

