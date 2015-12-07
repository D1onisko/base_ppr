# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base_ppr', '0007_auto_20151207_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Actionhistory title')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('comment', models.TextField(max_length=255, verbose_name='Comment')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated', db_index=True)),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': '',
                'verbose_name_plural': '\u0418\u0441\u0442\u043e\u0440\u0438\u044f',
            },
        ),
        migrations.RemoveField(
            model_name='itemhistory',
            name='item',
        ),
        migrations.RemoveField(
            model_name='itemhistory',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='action',
            name='slug',
        ),
        migrations.AlterField(
            model_name='action',
            name='priority',
            field=models.IntegerField(verbose_name='Priory'),
        ),
        migrations.AlterField(
            model_name='action',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Action title'),
        ),
        migrations.DeleteModel(
            name='ItemHistory',
        ),
        migrations.AddField(
            model_name='actionhistory',
            name='action',
            field=models.ForeignKey(related_name='entries', verbose_name='Action', to='base_ppr.Action'),
        ),
        migrations.AddField(
            model_name='actionhistory',
            name='user_name',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
