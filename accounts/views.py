from django.shortcuts import render, redirect
# from models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def signin(request):
    template_name = 'accounts/Sign-In.html'
    args = {}
    return render(request,template_name,args)


def signup(request):
    template_name = 'accounts/Sign-Up.html'
    args = {}
    return render(request,template_name,args)


def dashboard(request):
    template_name = 'accounts/dashboard.html'
    args = {}
    return render(request,template_name,args)


def questions(request):
    template_name = 'accounts/questions.html'
    args = {}
    return render(request,template_name,args)

def result(request):
    template_name = 'accounts/result.html'
    args = {}
    return render(request,template_name,args)