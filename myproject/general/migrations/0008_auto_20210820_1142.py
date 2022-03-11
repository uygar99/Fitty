# Generated by Django 3.2.5 on 2021-08-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_alter_trainer_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='photo',
            field=models.ImageField(blank=True, default='../static/images/default_profile.jpg', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='photo',
            field=models.ImageField(blank=True, default='default_profile.jpg', null=True, upload_to='media/'),
        ),
    ]