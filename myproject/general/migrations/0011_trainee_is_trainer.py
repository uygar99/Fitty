# Generated by Django 3.2.5 on 2021-08-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_remove_trainee_is_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='is_trainer',
            field=models.BooleanField(default=False),
        ),
    ]
