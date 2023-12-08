from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == "POST":
	    print("=="*20)
	    email = request.POST.get("email")
	    password = request.POST.get("password")
	    print(email, password)
	    print("=="*20)
    return render(request, 'authentication/html/login.html')