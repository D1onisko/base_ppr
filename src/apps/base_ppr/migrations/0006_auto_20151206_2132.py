# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_ppr', '0005_itemhistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemhistory',
            options={'ordering': ['-date_created'], 'verbose_name': 'ItemHistory', 'verbose_name_plural': 'ItemHistory'},
        ),
        migrations.AlterField(
            model_name='itemhistory',
            name='item',
            field=models.ForeignKey(related_name='entries', verbose_name='Item', to='base_ppr.Item'),
        ),
    ]
