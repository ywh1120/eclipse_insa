# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0013_auto_20151014_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academic',
            old_name='academic_trial',
            new_name='academic_trial_end',
        ),
        migrations.AddField(
            model_name='academic',
            name='academic_trial_start',
            field=models.DateField(null=True),
        ),
    ]
