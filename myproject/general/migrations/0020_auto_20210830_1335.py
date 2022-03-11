# Generated by Django 3.2.5 on 2021-08-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0019_auto_20210828_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='workout_list',
            field=models.ManyToManyField(blank=True, related_name='workout', to='general.Workout'),
        ),
    ]
