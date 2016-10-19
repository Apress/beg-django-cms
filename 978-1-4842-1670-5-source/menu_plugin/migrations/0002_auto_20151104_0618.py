# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('menu_plugin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaxEntries',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', auto_created=True, serialize=False, parent_link=True, primary_key=True)),
                ('max_entries', models.SmallIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='hello',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='Hello',
        ),
    ]
