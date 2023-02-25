from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, "home.html")


def send_to_home(request):
    return redirect(home)


def contact_us(request):
    return render(request, "contact_us.html")

    
def our_company(request):
    return render(request, "our_company.html")