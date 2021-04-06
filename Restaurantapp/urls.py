from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('ContactForm/', views.Contact, name = 'ContactForm'),
    path('LoginForm/', views.LoginForm, name = 'LoginForm'),
    path('Logout/', views.Logout, name = 'Logout'),
    path('RegisterForm/', views.Register, name = 'RegisterForm'),
    path('OrderNow/', views.OrderNow, name = 'OrderNow'),
    path('trial/', views.trial, name = 'trial')
]