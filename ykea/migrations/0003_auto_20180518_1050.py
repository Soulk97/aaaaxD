# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-18 10:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ykea', '0002_auto_20180518_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemquantity',
            name='pene',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='price',
        ),
    ]
