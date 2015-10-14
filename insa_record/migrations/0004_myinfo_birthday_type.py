# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0003_auto_20150928_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinfo',
            name='birthday_type',
            field=models.IntegerField(default=1),
        ),
    ]
