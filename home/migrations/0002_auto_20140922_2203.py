# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galeryimage',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='galeryitem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='galeryitem',
            name='title',
        ),
        migrations.AddField(
            model_name='galeryimage',
            name='description',
            field=models.TextField(default=datetime.date(2014, 9, 22)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='part',
            field=models.CharField(unique=True, max_length=1, choices=[(b'0', b'Intro'), (b'1', b'Biography')]),
        ),
    ]
