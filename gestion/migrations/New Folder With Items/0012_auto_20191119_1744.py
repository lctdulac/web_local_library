# Generated by Django 2.2.7 on 2019-11-19 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0011_auto_20191119_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='premier_retard',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]