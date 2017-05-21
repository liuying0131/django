# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0029_auto_20170520_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='studid',
            new_name='stuid',
        ),
    ]
