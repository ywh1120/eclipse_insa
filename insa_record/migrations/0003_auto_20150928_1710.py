# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0002_auto_20150928_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinfo',
            name='gender',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='house_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='married',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='military_serve',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='military_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
