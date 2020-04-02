from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.signin, name = 'Sign_In'),
    url(r"^signup", views.signup, name = 'Sign_Up'),
    url(r"dashboard", views.dashboard, name = 'Dashboard'),
    url(r"questions", views.questions, name = 'Questions'),
    url(r"result", views.result, name = 'Result'),   
    url(r"^create-user/$", views.signup_api, name = 'create-user'),  
    url(r"^login/$", views.login_api, name = 'login-user'),  
] 
