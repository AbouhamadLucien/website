

from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Create a new User object with the form data
            user = User(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                gender=form.cleaned_data['gender'],
                skill_level=form.cleaned_data['skill_level'],
                password=form.cleaned_data['password']
            )
            # Save the User object to the database
            user.save()
            # Redirect to a success page or log in the user
            
    
    return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'home.html')
