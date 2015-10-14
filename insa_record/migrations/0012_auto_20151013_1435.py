# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0011_auto_20151006_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eduinfo',
            name='edu_trial',
        ),
        migrations.AddField(
            model_name='eduinfo',
            name='edu_trial_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='eduinfo',
            name='edu_trial_start',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='academic_trial',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appoint_apday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='eduinfo',
            name='edu_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='family_birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='lang_getday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='license_getday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='rewardnpunish',
            name='rnp_punish_date',
            field=models.DateField(null=True),
        ),
    ]
