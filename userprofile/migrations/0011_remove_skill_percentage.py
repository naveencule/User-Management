# Generated by Django 5.1 on 2024-08-21 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_remove_profile_education_education'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='percentage',
        ),
    ]
