# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0026_auto_20170519_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acaname', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6_\xe9\x99\xa2')),
                ('stuid', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6_\xe5\x8f\xb7')),
                ('username', models.CharField(max_length=50, verbose_name=b'\xe5\xa7\x93_\xe5\x90\x8d')),
                ('grade1', models.CharField(max_length=50, verbose_name=b'\xe8\x8b\xb1_\xe8\xaf\xad')),
                ('grade2', models.CharField(max_length=50, verbose_name=b'\xe9\xab\x98_\xe6\x95\xb0')),
                ('grade3', models.CharField(max_length=50, verbose_name=b'\xe5\xa4\xa7_\xe7\x89\xa9')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index1', models.CharField(max_length=50, verbose_name=b'\xe6\x80\x9d\xe6\x83\xb3\xe5\x93\x81\xe5\xbe\xb7')),
                ('index2', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6\xe4\xb9\xa0\xe6\x88\x90\xe7\xbb\xa9')),
                ('index3', models.CharField(max_length=50, verbose_name=b'\xe8\xba\xab\xe4\xbd\x93\xe7\xb4\xa0\xe8\xb4\xa8')),
                ('index4', models.CharField(max_length=50, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe8\x83\xbd\xe5\x8a\x9b')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acaname', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6_\xe9\x99\xa2')),
                ('classnum', models.CharField(max_length=50, verbose_name=b'\xe7\x8f\xad_\xe7\xba\xa7')),
                ('stuid', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6_\xe5\x8f\xb7')),
                ('username', models.CharField(max_length=50, verbose_name=b'\xe5\xa7\x93_\xe5\x90\x8d')),
                ('sex', models.CharField(max_length=1, verbose_name=b'\xe6\x80\xa7_\xe5\x88\xab', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='student',
            field=models.ForeignKey(to='form_app.Student'),
            preserve_default=True,
        ),
    ]
