# views.py
from django.shortcuts import render
from .models import Band
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def home(request):
    """
    View for the home page.
    Retrieves all bands from the database and passes them to the 'home.html' template.
    """
    bands = Band.objects.all()
    return render(request, 'home.html', {'bands': bands})

def about(request):
    """
    View for the about page.
    Renders the 'about.html' template.
    """
    return render(request, 'about.html')

def contact(request):
    """
    View for the contact page.
    Renders the 'contact.html' template.
    """
    return render(request, 'contact.html')

def registration(request):
    """
    View for user registration.
    Handles user registration using Django's UserCreationForm.
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
