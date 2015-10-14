# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0012_auto_20151013_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='career_trial',
        ),
        migrations.AddField(
            model_name='career',
            name='career_trial_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='career_trial_start',
            field=models.DateField(null=True),
        ),
    ]
