# Generated by Django 5.0.1 on 2024-01-07 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='s_id',
            new_name='id',
        ),
    ]
