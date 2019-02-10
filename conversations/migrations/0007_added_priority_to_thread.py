# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-09 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0006_move_metadata_to_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='priority',
            field=models.IntegerField(choices=[(0, 'Low'), (10, 'Medium'), (100, 'High')], default=10),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('f4af2833-fba0-4e6d-9835-a35d122c01d0')),
        ),
        migrations.AlterField(
            model_name='thread',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Reopened'), (2, 'Waiting'), (3, 'Staff Replied'), (4, 'User Replied'), (5, 'Completed')], default=0),
        ),
    ]