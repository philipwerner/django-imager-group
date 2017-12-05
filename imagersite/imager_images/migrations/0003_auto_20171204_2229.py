# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 22:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_auto_20171203_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='imager_profile.ImagerProfile'),
        ),
    ]