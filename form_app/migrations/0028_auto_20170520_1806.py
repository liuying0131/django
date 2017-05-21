# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0027_auto_20170519_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='student',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6\xe5\x8f\xb7'),
            preserve_default=True,
        ),
    ]
