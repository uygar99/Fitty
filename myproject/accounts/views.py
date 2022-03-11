from django.contrib.auth import login as auth_login, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django import forms
from .forms import TrainerSignUpForm, TraineeSignUpForm
from django.views import View
from django.contrib import messages
from general.models import Trainer, Trainee
from django.contrib.auth.models import User


class SignUp(View):
    def get(self, request, *args, **kwargs):
        return render(request, '../templates/signup_choices.html')


class TrainerSignUp(View):
    model = Trainer

    def post(self, request, *args, **kwargs):
        form = TrainerSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['trainer_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            if password and password_again and password != password_again:
                return render(request, 'signup.html', context={'form': form})
            user = User(username=username, password=password, email=email)
            user.save()
            trainer = form.save(commit=False)
            trainer.user_id = user.id
            trainer.save()
            auth_login(request, user)
            messages.success(request, "You registered")
            return redirect('home')
        else:
            messages.error(request, "Registration is not successful")
        return render(request, 'signup.html', context={'form': form})

    def get(self, request, *args, **kwargs):
        form = TrainerSignUpForm()
        return render(request, 'signup.html', context={'form': form})

    """def clean_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("password_again")
        if password != confirm_password:
            raise forms.ValidationError("Passwords must match.")
        return password"""


class TraineeSignUp(View):
    model = Trainee

    def post(self, request, *args, **kwargs):
        form = TraineeSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['trainee_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            if password and password_again and password != password_again:
                return render(request, 'signup.html', context={'form': form})
            user = User(username=username, password=password, email=email)
            user.save()
            trainee = form.save(commit=False)
            trainee.user_id = user.id
            trainee.save()
            auth_login(request, user)
            messages.success(request, "You registered")
            return redirect('home')
        else:
            messages.error(request, "Registration is not successful")
        return render(request, 'signup.html', context={'form': form})

    def get(self, request, *args, **kwargs):
        form = TraineeSignUpForm()
        return render(request, 'signup.html', context={'form': form})

    """def clean_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("password_again")
        if password != confirm_password:
            raise forms.ValidationError("Passwords must match.")
        return password"""


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {'login_form': form}
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

        else:
            context = {'login_form': form}
            return render(request, 'accounts/login.html', context)
