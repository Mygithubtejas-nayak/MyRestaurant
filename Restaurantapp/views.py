from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

def homepage(request):
    return render(request, 'Restaurantapp/homepage.html', )


def Contact(request):

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ContactForm')

    
    return render(request, 'Restaurantapp/Contactform.html', {'Form' : form})