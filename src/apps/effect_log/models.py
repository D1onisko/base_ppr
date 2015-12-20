# -*- coding: utf-8 -*-
import os
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import mptt
from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify


def custom_slugify(value):
    # для перевода в кирилицу нужно установить pytils==0.3
    return default_slugify(value).replace('-', '_')


class Category(MPTTModel):
    """
    Description models
    """
    parent = TreeForeignKey(u'self', verbose_name='Parent', blank=True, null=True, related_name=u'children')
    user_name = models.ForeignKey(User, related_name='+', to_field=u"username")
    name = models.CharField(verbose_name='Name', max_length=255, db_index=True)
    description = models.TextField(verbose_name='Description', blank=True)
    slug = AutoSlugField(populate_from='name', slugify=custom_slugify, unique=True)
    date_created = models.DateTimeField(verbose_name="Date created", auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Is active', default=None)

    class Meta:
        ordering = ['-date_created']
        verbose_name = u'Категория'
        verbose_name_plural = u'Категория'

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'level'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('effect_log:category', args=[self.slug])

mptt.register(Category)

class EffectLog(models.Model):
    """
    Журнал эффективности
    """
    TECHNICAL, OPERATOR, PROIZVODSTVO = u'Технический простой', u'Простой по вине оператора', u'Производственный простой'
    STRUCTURE_CHOICES = (
        (TECHNICAL, u'Технический простой'),
        (OPERATOR, u'Простой по вине оператора'),
        (PROIZVODSTVO, u'Производственный простой')
    )
    category = TreeForeignKey(Category, verbose_name='Category', related_name='entries',)
    user_name = models.ForeignKey(User, related_name='+', to_field=u"username")
    operator = models.CharField(verbose_name='Operator', max_length=20)
    type_prostoy = models.CharField(verbose_name="Type Prostoya", max_length=40, choices=STRUCTURE_CHOICES, default=TECHNICAL)
    time_prostoy = models.TimeField(verbose_name='Time Prostoya')
    dlitelnost_prostoya = models.IntegerField(verbose_name=' Dlitelnost prostoya')
    comments = models.TextField(verbose_name='Comments')
    date_created = models.DateTimeField(verbose_name="Date created", auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = u'Журнал эффективности'
        verbose_name_plural = u'Журнал эффективности'

    def get_absolute_url(self):
        return reverse('core:index', args=[str(self.pk)])


