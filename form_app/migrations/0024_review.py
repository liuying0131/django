# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0023_auto_20170519_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index1', models.CharField(max_length=50, verbose_name=b'\xe6\x80\x9d\xe6\x83\xb3\xe5\x93\x81\xe5\xbe\xb7')),
                ('index2', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6\xe4\xb9\xa0\xe6\x88\x90\xe7\xbb\xa9')),
                ('index3', models.CharField(max_length=50, verbose_name=b'\xe8\xba\xab\xe4\xbd\x93\xe7\xb4\xa0\xe8\xb4\xa8')),
                ('index4', models.CharField(max_length=50, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe8\x83\xbd\xe5\x8a\x9b')),
                ('student', models.ForeignKey(to='form_app.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
