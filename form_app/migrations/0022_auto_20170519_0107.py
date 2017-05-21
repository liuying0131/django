# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0021_auto_20170519_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='student',
            field=models.ForeignKey(to='form_app.Student'),
            preserve_default=True,
        ),
    ]
