# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paste_text', models.TextField()),
                ('paste_name', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='Created at')),
            ],
        ),
    ]
