# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 21:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuffdb', '0003_auto_20160520_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maker',
            name='role',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]