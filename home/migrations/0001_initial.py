# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GaleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('large', imagekit.models.fields.ProcessedImageField(upload_to=b'pictures/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GaleryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ManyToManyField(to='home.GaleryImage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part', models.CharField(unique=True, max_length=1, choices=[(b'0', b'Intro'), (b'1', b'Biography'), (b'2', b'Contact')])),
                ('header', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('background', imagekit.models.fields.ProcessedImageField(upload_to=b'pictures/')),
            ],
            options={
                'ordering': ['part'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='galeryitem',
            name='tag',
            field=models.ManyToManyField(to='home.Tag'),
            preserve_default=True,
        ),
    ]
