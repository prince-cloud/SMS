# Generated by Django 3.0.7 on 2020-06-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20200614_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
