# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0035_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='stuid',
            new_name='student',
        ),
    ]
