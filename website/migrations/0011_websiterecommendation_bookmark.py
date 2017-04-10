# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 17:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0010_auto_20170313_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiterecommendation',
            name='bookmark',
            field=models.ManyToManyField(related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]