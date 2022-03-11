from django import forms
from django.contrib.auth.models import User
from general.models import Trainee, Trainer
from django.forms import ModelForm


class TraineeSignUpForm(ModelForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    trainee_name = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Trainee
        fields = ('trainee_name', 'email', 'password', 'password_again')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            self.add_error("email", "A user with this email already exists.")
        return email


class TrainerSignUpForm(ModelForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    trainer_name = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Trainer
        fields = ('trainer_name', 'password', 'password_again', 'email', 'description', 'photo', 'proficiency')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            self.add_error("email", "A user with this email already exists.")
        return email

    def clean_password2(self):
        print(self.cleaned_data)
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_again')
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError(_('Your passwords do not match'), code='invalid')
        return password2
