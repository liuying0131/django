# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0043_auto_20170521_0945'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
