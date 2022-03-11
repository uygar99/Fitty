# Generated by Django 3.2.5 on 2021-08-11 13:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainee',
            name='target_height',
        ),
        migrations.AlterField(
            model_name='workout',
            name='difficulty',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]