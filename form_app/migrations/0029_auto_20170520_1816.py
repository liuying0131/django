# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0028_auto_20170520_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='student',
            new_name='studid',
        ),
    ]
