# Generated by Django 3.2.5 on 2021-08-12 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_rename_followers_trainee_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='workout_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainee', to='general.workoutlist'),
        ),
    ]
