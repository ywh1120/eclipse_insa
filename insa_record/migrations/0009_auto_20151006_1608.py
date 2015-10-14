# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0008_auto_20151006_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myinfo',
            name='info_image',
            field=models.ImageField(null=True, upload_to=b'static_files/uploaded/%Y/%m/%d'),
        ),
    ]
