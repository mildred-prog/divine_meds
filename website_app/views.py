from django.shortcuts import render

def home(request):
    return render(request, "website_app/home.html")
