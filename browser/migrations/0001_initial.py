# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('origin', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('imageURL', models.URLField()),
                ('buyURL', models.URLField()),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('minAge', models.PositiveSmallIntegerField(default=5)),
                ('maxAge', models.PositiveSmallIntegerField(default=15)),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
