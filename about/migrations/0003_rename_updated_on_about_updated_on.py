# Generated by Django 4.2.8 on 2024-01-04 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_updated_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='Updated_on',
            new_name='updated_on',
        ),
    ]
