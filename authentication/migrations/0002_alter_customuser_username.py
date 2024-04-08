# Generated by Django 4.2.9 on 2024-04-08 10:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\-_]+\\Z', 'Only letters, hyphens, and underscores are allowed.')], verbose_name='username'),
        ),
    ]
