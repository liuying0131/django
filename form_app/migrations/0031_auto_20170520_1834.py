# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0030_auto_20170520_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='index1',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x80\x9d\xe6\x83\xb3\xe5\x93\x81\xe5\xbe\xb7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='index2',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xad\xa6\xe4\xb9\xa0\xe6\x88\x90\xe7\xbb\xa9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='index3',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe8\xba\xab\xe4\xbd\x93\xe7\xb4\xa0\xe8\xb4\xa8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='index4',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe8\x83\xbd\xe5\x8a\x9b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='stuid',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xad\xa6\xe5\x8f\xb7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='acaname',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xad\xa6_\xe9\x99\xa2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='classnum',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe7\x8f\xad_\xe7\xba\xa7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(max_length=1, null=True, verbose_name=b'\xe6\x80\xa7_\xe5\x88\xab', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='stuid',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xad\xa6_\xe5\x8f\xb7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xa7\x93_\xe5\x90\x8d'),
            preserve_default=True,
        ),
    ]
