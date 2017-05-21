# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0031_auto_20170520_1834'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
