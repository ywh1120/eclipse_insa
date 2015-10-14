# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myinfo',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='myinfo',
            name='house_type',
        ),
        migrations.RemoveField(
            model_name='myinfo',
            name='married',
        ),
        migrations.RemoveField(
            model_name='myinfo',
            name='military_serve',
        ),
        migrations.RemoveField(
            model_name='myinfo',
            name='military_type',
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='employ_day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='handicap_trial',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='retire_date',
            field=models.DateField(),
        ),
    ]
