# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField(verbose_name=b'Priority')),
                ('description_action', models.TextField(verbose_name=b'Description action', blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name=b'Date updated', db_index=True)),
                ('user_name', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': '\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f',
            },
        ),
    ]
