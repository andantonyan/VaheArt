# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20140922_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeryitem',
            name='title',
            field=models.CharField(default=datetime.date(2014, 9, 22), max_length=300),
            preserve_default=False,
        ),
    ]
