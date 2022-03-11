from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

WORKOUT_CHOICES = [(0, 'Yoga'), (1, 'Push'), (2, 'Pull'), (3, 'Legs'), (4, 'Upper'), (5, 'Lower'), (6, 'Shoulders'),
                   (7, 'Pectoral'), (8, 'ABS'), (9, 'Arms'), (10, 'Back'), (11, 'Boxing'), (12, 'Swimming'),
                   (13, 'Gym_cardio'), (14, 'Bodyweight_cardio'), (15, 'Calisthenics')]

STATUS_CHOICES = [(0, 'todo'), (1, 'done')]


class Trainer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    description = models.CharField(max_length=500)
    proficiency = models.CharField(max_length=100)
    photo = models.ImageField(default="../static/images/default_profile.jpg", null=True, blank=True, upload_to='media/')


class Workout(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    working_muscles = models.CharField(max_length=100)
    photo = models.ImageField(default="default_profile.jpg", null=True, blank=True, upload_to='media/')
    last_updated = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True, null=True)
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    click_count = models.IntegerField(null=True)
    trainer = models.ForeignKey(Trainer, related_name='routines', on_delete=models.CASCADE)
    workout_type = models.IntegerField(choices=WORKOUT_CHOICES, default=0)
    url = models.URLField(null=True)


class Trainee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    boyun = models.FloatField(null=True, blank=True)
    omuz = models.FloatField(null=True, blank=True)
    sag_kol = models.FloatField(null=True, blank=True)
    sol_kol = models.FloatField(null=True, blank=True)
    bel = models.FloatField(null=True, blank=True)
    alt_karin = models.FloatField(null=True, blank=True)
    sag_bacak = models.FloatField(null=True, blank=True)
    sol_bacak = models.FloatField(null=True, blank=True)
    kalca = models.FloatField(null=True, blank=True)
    sag_on_kol = models.FloatField(null=True, blank=True)
    sol_on_kol = models.FloatField(null=True, blank=True)
    body_fat = models.FloatField(null=True, blank=True)
    omuz_bel_orani = models.FloatField(null=True, blank=True)
    target_weight = models.FloatField(null=True, blank=True)
    target_boyun = models.FloatField(null=True, blank=True)
    target_omuz = models.FloatField(null=True, blank=True)
    target_sag_kol = models.FloatField(null=True, blank=True)
    target_sol_kol = models.FloatField(null=True, blank=True)
    target_bel = models.FloatField(null=True, blank=True)
    target_alt_karin = models.FloatField(null=True, blank=True)
    target_sag_bacak = models.FloatField(null=True, blank=True)
    target_sol_bacak = models.FloatField(null=True, blank=True)
    target_kalca = models.FloatField(null=True, blank=True)
    target_sag_on_kol = models.FloatField(null=True, blank=True)
    target_sol_on_kol = models.FloatField(null=True, blank=True)
    target_body_fat = models.FloatField(null=True, blank=True)
    target_omuz_bel_orani = models.FloatField(null=True, blank=True)
    workout_list = models.ManyToManyField(Workout, related_name='trainee')


class Status(models.Model):
    statuses = models.CharField(choices=[('To Do', 'To Do'), ('Done', 'Done')], default='To Do', max_length=30)
    trainee = models.ForeignKey(Trainee, related_name='status', null=True, blank=True, on_delete=models.PROTECT)
    workout = models.ForeignKey(Workout, related_name='status', null=True, blank=True, on_delete=models.PROTECT)