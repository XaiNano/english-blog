# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-10 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_tiles_pdf_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiles',
            name='pdf_path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.PDF'),
        ),
    ]
