# Generated by Django 4.2.7 on 2024-01-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_addressee_user_alter_addressee_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressee',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='addressee',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='addressee',
            name='surName',
        ),
        migrations.AddField(
            model_name='addressee',
            name='name',
            field=models.CharField(default=True, max_length=60),
        ),
        migrations.AddField(
            model_name='addressee',
            name='postal_code',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='addressee',
            name='address',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='addressee',
            name='city',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
