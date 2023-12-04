from django import forms
from .models import Contacts

# contact form

class ContactsForm(forms.ModelForm):
    
    class Meta:
        model = Contacts
        fields = ("name", "email", "subject", "message")
