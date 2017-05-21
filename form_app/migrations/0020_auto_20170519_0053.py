# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0019_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='stuid',
        ),
        migrations.AddField(
            model_name='review',
            name='student',
            field=models.ForeignKey(related_name='student_review', default=4161, to='form_app.Student'),
            preserve_default=False,
        ),
    ]
