# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0020_auto_20170519_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='userwork',
        ),
        migrations.AlterField(
            model_name='review',
            name='student',
            field=models.ForeignKey(related_name='student_review', to='form_app.Student'),
            preserve_default=True,
        ),
    ]
