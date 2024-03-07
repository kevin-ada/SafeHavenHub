import os

from django.conf import settings
from django.template import context
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def logout_view(request):
    logout(request)
    return redirect('sign_in')


def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        bio = request.POST['bio']
        location = request.POST['location']
        interests = request.POST['interests']

        # Validate form data: ensure that all fields are filled and that the email is unique
        if not all([email, password, bio, location, interests]):
            messages.error(request, 'All fields must be filled')
            return render(request, 'components/signup.html')

        if UserProfile.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'components/signup.html')

        # Create a new user
        user = UserProfile.objects.create_user(email=email, password=password)
        user.bio = bio
        user.location = location
        user.interests = interests
        user.save()

        # Log the user in
        login(request, user)

        # Redirect to a success page
        return redirect('home')

    else:
        return render(request, 'components/signup.html')


def sign_in_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'components/sign_in.html')
    else:
        messages.info(request, "You Need to be Signed In to Create an Event Or Blog")
        return render(request, 'components/sign_in.html')


class HomeView(TemplateView):
    template_name = 'components/index.html'


class AboutUsView(TemplateView):
    template_name = 'components/about-us.html'


class ContactUsView(TemplateView):
    template_name = 'components/contact_us.html'
