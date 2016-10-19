# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_plugin', '0002_auto_20151104_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maxentries',
            name='max_entries',
            field=models.SmallIntegerField(verbose_name='Maximum Entries', default=0),
            preserve_default=True,
        ),
    ]
