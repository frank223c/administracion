# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_factura',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]