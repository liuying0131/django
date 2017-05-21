# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0042_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade1',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe8\x8b\xb1_\xe8\xaf\xad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade2',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe9\xab\x98_\xe6\x95\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade3',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xa4\xa7_\xe7\x89\xa9'),
            preserve_default=True,
        ),
    ]
