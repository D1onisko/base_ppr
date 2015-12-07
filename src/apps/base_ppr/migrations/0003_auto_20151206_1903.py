# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import mptt.fields
import src.apps.base_ppr.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base_ppr', '0002_auto_20151206_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name', db_index=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, slugify=src.apps.base_ppr.models.custom_slugify)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date created')),
                ('is_active', models.BooleanField(default=None, verbose_name='Is active')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='Parent', blank=True, to='base_ppr.Category', null=True)),
                ('user_name', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='plan',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
