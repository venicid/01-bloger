# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-21 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aritcle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
