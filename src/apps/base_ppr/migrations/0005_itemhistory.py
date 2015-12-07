# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base_ppr', '0004_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Product title')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated', db_index=True)),
                ('item', mptt.fields.TreeForeignKey(related_name='entries', verbose_name='Item', to='base_ppr.Item')),
                ('user_name', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
    ]
