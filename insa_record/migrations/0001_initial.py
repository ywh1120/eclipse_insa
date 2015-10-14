# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trial', models.CharField(max_length=80)),
                ('school_title', models.CharField(max_length=80)),
                ('school_part', models.CharField(max_length=50)),
                ('graduated', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50)),
                ('apday', models.CharField(max_length=80)),
                ('part', models.CharField(max_length=60)),
                ('position', models.CharField(max_length=50)),
                ('work', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trial', models.CharField(max_length=80)),
                ('oldjob', models.CharField(max_length=80)),
                ('job_type', models.CharField(max_length=30)),
                ('job_position', models.CharField(max_length=30)),
                ('retire_reason', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Eduinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=100)),
                ('trial', models.CharField(max_length=80)),
                ('organization', models.CharField(max_length=60)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relation', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('birthday', models.CharField(max_length=80)),
                ('academic', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=50)),
                ('together', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=30)),
                ('grade', models.CharField(max_length=10)),
                ('score', models.IntegerField(default=0)),
                ('pubtest', models.CharField(max_length=50)),
                ('getday', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('number', models.CharField(max_length=50)),
                ('getday', models.CharField(max_length=80)),
                ('organization', models.CharField(max_length=60)),
                ('etc', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Myinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_kor', models.CharField(max_length=30)),
                ('name_eng', models.CharField(max_length=50)),
                ('civil_code', models.CharField(max_length=60)),
                ('gender', models.IntegerField(default=1)),
                ('married', models.IntegerField(default=0)),
                ('birthday', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=150)),
                ('address_civil', models.CharField(max_length=200)),
                ('address_live', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('mobile_phone', models.CharField(max_length=100)),
                ('head_house', models.CharField(max_length=60)),
                ('house_type', models.IntegerField(default=1)),
                ('handicap_type', models.CharField(max_length=30)),
                ('handicap_grade', models.IntegerField(default=1)),
                ('handicap_trial', models.CharField(max_length=80)),
                ('handicap_num', models.CharField(max_length=100)),
                ('handicap_div', models.CharField(max_length=100)),
                ('military_serve', models.IntegerField(default=1)),
                ('military_type', models.IntegerField(default=1)),
                ('military_branch', models.CharField(max_length=30)),
                ('military_exampt', models.CharField(max_length=80)),
                ('military_class', models.CharField(max_length=20)),
                ('employ_day', models.CharField(max_length=80)),
                ('employ_part', models.CharField(max_length=30)),
                ('employ_kind', models.CharField(max_length=30)),
                ('employ_type', models.IntegerField(default=1)),
                ('employ_intro', models.CharField(max_length=50)),
                ('employ_etc', models.CharField(max_length=60)),
                ('emergency_name', models.CharField(max_length=30)),
                ('emergency_rel', models.CharField(max_length=20)),
                ('emergency_address', models.CharField(max_length=200)),
                ('emergency_call', models.CharField(max_length=80)),
                ('sign', models.CharField(max_length=150)),
                ('retire_date', models.CharField(max_length=80)),
                ('retire_reason', models.CharField(max_length=150)),
                ('info_image', models.ImageField(upload_to=b'')),
                ('etc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rewardnpunish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reward_date', models.CharField(max_length=80)),
                ('reward_content', models.CharField(max_length=150)),
                ('reward_result', models.CharField(max_length=80)),
                ('punish_date', models.CharField(max_length=80)),
                ('punish_content', models.CharField(max_length=150)),
                ('punish_result', models.CharField(max_length=80)),
                ('myinfo', models.ForeignKey(to='insa_record.Myinfo')),
            ],
        ),
        migrations.AddField(
            model_name='license',
            name='myinfo',
            field=models.ForeignKey(to='insa_record.Myinfo'),
        ),
        migrations.AddField(
            model_name='language',
            name='myinfo',
            field=models.ForeignKey(to='insa_record.Myinfo'),
        ),
        migrations.AddField(
            model_name='family',
            name='myinfo',
            field=models.ForeignKey(to='insa_record.Myinfo'),
        ),
        migrations.AddField(
            model_name='eduinfo',
            name='myinfo',
            field=models.ForeignKey(to='insa_record.Myinfo'),
        ),
        migrations.AddField(
            model_name='career',
            name='myinfo',
            field=models.ForeignKey(to='insa_record.Myinfo'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='myinfo',
            field=models.ForeignKey(to='insa_record.Myinfo'),
        ),
        migrations.AddField(
            model_name='academic',
            name='myinfo',
            field=models.ForeignKey(to='insa_record.Myinfo'),
        ),
    ]
