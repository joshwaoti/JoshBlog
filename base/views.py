from django.shortcuts import render, redirect
from .models import Contacts
from .forms import ContactsForm

def home(request):
    return render(request, 'base/home.html')


def contactPage(request):
    if request.method == "POST":
        form = ContactsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact')
        
    else:
        form = ContactsForm()

    return render(request, "base/contact.html", {"form": form})
