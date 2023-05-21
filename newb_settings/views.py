from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "index.html")


def send_to_home(request):
    return redirect(index)
