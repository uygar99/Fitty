# Generated by Django 3.2.5 on 2021-08-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_trainee_target_omuz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='photo',
            field=models.ImageField(blank=True, default='default_profile.png', null=True, upload_to='media/'),
        ),
    ]