# Generated by Django 4.2.7 on 2024-01-04 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_customuser_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='type',
        ),
    ]
