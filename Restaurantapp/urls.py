from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('ContactForm/', views.Contact, name = 'ContactForm'),
    path('LoginForm/', views.Login, name = 'LoginForm'),
    path('RegisterForm/', views.Register, name = 'RegisterForm')
]