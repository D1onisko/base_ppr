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
        ('base_ppr', '0006_auto_20151206_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Product title')),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'title', editable=False, slugify=src.apps.base_ppr.models.custom_slugify)),
                ('priority', models.IntegerField(verbose_name='Price')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated', db_index=True)),
                ('is_discountable', models.BooleanField(default=True, verbose_name='Is discountable?')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': '',
                'verbose_name_plural': '\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c',
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='user_name',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-date_created'], 'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='itemhistory',
            options={'ordering': ['-date_created'], 'verbose_name': '', 'verbose_name_plural': '\u0418\u0441\u0442\u043e\u0440\u0438\u044f'},
        ),
        migrations.AlterField(
            model_name='itemhistory',
            name='item',
            field=models.ForeignKey(related_name='entries', verbose_name='Item', to='base_ppr.Action'),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='action',
            name='category',
            field=mptt.fields.TreeForeignKey(related_name='entries', verbose_name='Category', to='base_ppr.Category'),
        ),
        migrations.AddField(
            model_name='action',
            name='user_name',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
