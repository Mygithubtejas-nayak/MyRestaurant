from django import  forms
from .models import ContactUS

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactUS
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.TextInput(attrs={'class' : 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class' : 'form-control'}),
            'Query': forms.Textarea(attrs={'class' : 'form-control', 'rows' : '3'})

        }
