# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 16:09
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0004_capitalizeverbose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploaded_by_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user'),
        ),
    ]
