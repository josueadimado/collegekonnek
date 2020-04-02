from django.shortcuts import render, redirect, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
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


@csrf_exempt
def signup_api(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val
    user = Student()
    try:
        user.username = objects['email']
    except Exception as e:
        data = {
        'success':False,
        'message':str(e)
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

    user.email = objects['email']
    user.gender = objects['gender']
    user.save()
    user.set_password(objects['password'])
    user.first_name = objects['first_name']
    user.last_name = objects['last_name']
    user.save()
    data = {
        'success':True,
        'message':'user created'
    }
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')



@csrf_exempt
def login_api(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val
    user = authenticate(request,username=objects['username'],password=objects['password'])
    if user is not None:
        login(request,user)
        messages.success(request,"login succeful")
        data = {
        'success':True,
        'message':'Login succeful'
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')
    else:
        messages.error(request,"Please check your email or password well.")
        data = {
        'success':False,
        'message':'Please check your credentials'
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')
