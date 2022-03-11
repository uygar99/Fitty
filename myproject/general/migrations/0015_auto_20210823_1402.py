# Generated by Django 3.2.5 on 2021-08-23 11:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0014_remove_trainee_is_trainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='is_trainer',
        ),
        migrations.AddField(
            model_name='workout',
            name='workout_type',
            field=models.IntegerField(choices=[(0, 'Yoga'), (1, 'Push'), (2, 'Pull'), (3, 'Legs'), (4, 'Upper'), (5, 'Lower'), (6, 'Shoulders'), (7, 'Pectoral'), (8, 'ABS'), (10, 'Arms'), (11, 'Back'), (12, 'Boxing'), (13, 'Swimming'), (14, 'Gym_cardio'), (15, 'Bodyweight_cardio'), (16, 'Calisthenics')], default=0),
        ),
        migrations.AlterField(
            model_name='workout',
            name='difficulty',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]