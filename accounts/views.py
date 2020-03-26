from django.shortcuts import render, redirect
# from models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def signin(request):
    template_name = 'accounts/Sign-In.html'
    args = {}
    return render(request,template_name,args)
