# Generated by Django 4.2.7 on 2024-01-04 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_remove_addressee_firstname_remove_addressee_mail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressee',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
