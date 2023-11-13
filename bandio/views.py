from django.shortcuts import render
from .models import Band
from django.contrib.auth.forms import UserCreationForm  # Import Django's UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    # Retrieve all bands from the database and pass them to the 'home.html' template
    bands = Band.objects.all()
    return render(request, 'home.html', {'bands': bands})

def about(request):
    # Render the 'about.html' template
    return render(request, 'about.html')

def contact(request):
    # Render the 'contact.html' template
    return render(request, 'contact.html')

def registration(request):
    # Handle user registration using Django's UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()  # Create a new UserCreationForm for GET requests
    return render(request, 'registration/registration.html', {'form': form})
