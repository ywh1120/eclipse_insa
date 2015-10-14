# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0015_auto_20151014_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myinfo',
            name='employ_etc',
        ),
        migrations.AddField(
            model_name='myinfo',
            name='etc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
