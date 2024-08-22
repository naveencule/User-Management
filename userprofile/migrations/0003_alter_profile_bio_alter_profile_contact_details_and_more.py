# Generated by Django 5.1 on 2024-08-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_profile_profile_picture_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_details',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
    ]
