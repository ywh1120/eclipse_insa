# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0014_auto_20151014_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myinfo',
            old_name='etc',
            new_name='pay_step',
        ),
        migrations.AddField(
            model_name='myinfo',
            name='salary_class',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
