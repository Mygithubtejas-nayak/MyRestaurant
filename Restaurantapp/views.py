from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import ContactForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request, 'Restaurantapp/homepage.html')

@login_required(login_url='LoginForm')
def OrderNow(request):
    return render(request, 'Restaurantapp/OrderNow.html')

def trial(request):
    return render(request, 'Restaurantapp/trial.html')


def LoginForm(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/OrderNow')
            else:
                messages.info(request, 'Username OR Password is incorrect')
            
        return render(request, 'Restaurantapp/LoginForm.html')



def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.info(request, 'Username OR Password is incorrect')
            
        return render(request, 'Restaurantapp/LoginForm.html')


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/LoginForm')


def Register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:    
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + ' user was created')
                return HttpResponseRedirect('/LoginForm')

        context = {'form' : form}
        return render(request, 'Restaurantapp/RegisterForm.html', context)


def Contact(request):

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ContactForm')

    
    return render(request, 'Restaurantapp/Contactform.html', {'Form' : form})