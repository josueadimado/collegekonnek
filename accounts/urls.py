from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.signin, name = 'Sign_In'),
    url(r"sign_up", views.signup, name = 'Sign_Up'),
    url(r"dashboard", views.dashboard, name = 'Dashboard'),
    url(r"questions", views.questions, name = 'Questions'),
] 
