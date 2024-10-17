from django.shortcuts import render
from django.http import HttpResponse

# view cadastro
def cadastro(request):
    return render(request, 'cadastro.html')

# view login
def login(request):
    return render(request, 'login.html')
