# Generated by Django 3.0.7 on 2020-06-13 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_lecturer',
            new_name='is_teacher',
        ),
    ]