# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teryt_tree', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='jednostkaadministracyjna',
            options={'verbose_name': 'Unit of administrative division', 'verbose_name_plural': 'Units of administrative division'},
        ),
        migrations.AlterField(
            model_name='category',
            name='level',
            field=models.IntegerField(db_index=True, choices=[(1, 'voivodeship'), (2, 'county'), (3, 'community')]),
        ),
        migrations.AlterField(
            model_name='jednostkaadministracyjna',
            name='updated_on',
            field=models.DateField(verbose_name='Updated date'),
        ),
    ]
