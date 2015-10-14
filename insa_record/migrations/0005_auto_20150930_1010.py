# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insa_record', '0004_myinfo_birthday_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='graduated',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='school_part',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='school_title',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='trial',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='apday',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='part',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='position',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='work',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='job_position',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='job_type',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='oldjob',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='retire_reason',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='trial',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='eduinfo',
            name='cost',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='eduinfo',
            name='organization',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='eduinfo',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='eduinfo',
            name='trial',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='eduinfo',
            name='type',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='academic',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='birthday',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='job',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='relation',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='together',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='getday',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='grade',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='pubtest',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='etc',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='getday',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='organization',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='title',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='etc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='handicap_div',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='handicap_num',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='handicap_trial',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='handicap_type',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='info_image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='military_branch',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='military_class',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='military_exampt',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='retire_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='retire_reason',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='rewardnpunish',
            name='punish_content',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='rewardnpunish',
            name='punish_date',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='rewardnpunish',
            name='punish_result',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='rewardnpunish',
            name='reward_content',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='rewardnpunish',
            name='reward_date',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='rewardnpunish',
            name='reward_result',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
