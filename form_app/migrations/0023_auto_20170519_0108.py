# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0022_auto_20170519_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='student',
        ),
        migrations.DeleteModel(
            name='review',
        ),
    ]
