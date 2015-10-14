# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0005_auto_20150930_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='myinfo',
            field=models.ForeignKey(to='insa_record.Myinfo', null=True),
        ),
    ]
