# Generated by Django 3.2.5 on 2021-08-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0015_auto_20210823_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='add_field1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='add_field2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='add_field3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='target_add_field1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='target_add_field2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='target_add_field3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
