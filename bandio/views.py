from django.shortcuts import render
from .models import Band
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def home(request):
    """
    Renders the home page.

    Retrieves all bands from the database and passes them to the 'home.html' template.
    """
    bands = Band.objects.all()
    return render(request, 'home.html', {'bands': bands})

def about(request):
    """
    Renders the about page.
    """
    return render(request, 'about.html')

def contact(request):
    """
    Renders the contact page.
    """
    return render(request, 'contact.html')

def registration(request):
    """
    Handles user registration using Django's UserCreationForm.

    If the form is valid, registers the user and redirects to the home page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})
