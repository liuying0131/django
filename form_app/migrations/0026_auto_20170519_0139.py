# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0025_auto_20170519_0113'),
    ]

    operations = [
        migrations.DeleteModel(
            name='grade',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
