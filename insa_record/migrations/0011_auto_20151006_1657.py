# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import insa_record.models


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0010_auto_20151006_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myinfo',
            name='info_image',
            field=models.ImageField(null=True, upload_to=insa_record.models.generate_filename),
        ),
    ]
