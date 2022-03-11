from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from flask import request

from .models import Trainee, Trainer, Workout, WORKOUT_CHOICES
from django.forms import ModelForm, Form


class EditStatisticsForm(ModelForm):

    class Meta:
        model = Trainee
        fields = ('height', 'weight', 'target_weight', 'boyun', 'target_boyun',
                  'omuz', 'target_omuz', 'sag_kol', 'target_sag_kol',
                  'sol_kol', 'target_sol_kol', 'bel', 'target_bel',
                  'alt_karin', 'target_alt_karin', 'sag_bacak',
                  'target_sag_bacak', 'sol_bacak', 'target_sol_bacak',
                  'kalca', 'target_kalca', 'sag_on_kol', 'target_sag_on_kol',
                  'sol_on_kol', 'target_sol_on_kol', 'body_fat', 'target_body_fat',
                  'omuz_bel_orani', 'target_omuz_bel_orani')


class AddWorkoutForm(ModelForm):

    class Meta:
        model = Workout
        fields = ('name', 'description', 'working_muscles', 'photo', 'difficulty',
                  'workout_type', 'url')


class EditTrainerForm(ModelForm):

    class Meta:
        model = Trainer
        fields = ('description', 'proficiency')


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ('photo',)


class EditTrainerUsernameForm(ModelForm):

    class Meta:
        model = User
        fields = ('username',)
