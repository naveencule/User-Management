# Generated by Django 5.1 on 2024-08-20 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_profile_contact_email_profile_contact_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contact_details',
        ),
    ]
