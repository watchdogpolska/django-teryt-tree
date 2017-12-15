# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import autoslug.fields
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', editable=False)),
                ('level', models.IntegerField(db_index=True, choices=[(1, 'wojew\xf3dztwo'), (2, 'powiat'), (3, 'gmina')])),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='JednostkaAdministracyjna',
            fields=[
                ('id', models.CharField(max_length=7, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=36, verbose_name='Nazwa')),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, editable=False)),
                ('updated_on', models.DateField(verbose_name='Data aktualizacji')),
                ('active', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('category', models.ForeignKey(to='teryt_tree.Category', on_delete=django.db.models.deletion.CASCADE)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', on_delete=django.db.models.deletion.CASCADE, blank=True, to='teryt_tree.JednostkaAdministracyjna', null=True)),
            ],
            options={
                'verbose_name': 'Jednostka podzia\u0142u terytorialnego',
                'verbose_name_plural': 'Jednostki podzia\u0142u terytorialnego',
            },
        ),
    ]
