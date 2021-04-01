from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def homepage(request):
    return render(request, 'Restaurantapp/homepage.html', )

def Login(request):
    return render(request, 'Restaurantapp/LoginForm.html')

def Register(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/RegisterForm')

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