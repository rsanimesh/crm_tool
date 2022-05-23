from django.shortcuts import render

def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def custom_admin(request):
    return render(request, 'custom_admin.html')
