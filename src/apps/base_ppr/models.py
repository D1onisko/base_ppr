# -*- coding: utf-8 -*-
import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _, pgettext_lazy

import mptt
from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager
from autoslug.settings import slugify as default_slugify
from autoslug import AutoSlugField

def custom_slugify(value):
    # для перевода в кирилицу нужно установить pytils==0.3
    return default_slugify(value).replace('-', '_')

@python_2_unicode_compatible
class Category(MPTTModel):
    """
    Description models
    """
    parent = TreeForeignKey(u'self', verbose_name=_(u'Parent'), blank=True, null=True, related_name=u'children')
    user_name = models.ForeignKey(User, related_name='+', to_field=u"username")
    name = models.CharField(_('Name'), max_length=255, db_index=True)
    slug = AutoSlugField(populate_from='name', slugify=custom_slugify, unique=True)
    date_created = models.DateTimeField(verbose_name="Date created", auto_now_add=True)
    is_active = models.BooleanField(verbose_name=_('Is active'), default=None)

    class Meta:
        ordering = ['-date_created']
        verbose_name = _(u'Категория')
        verbose_name_plural = _(u'Категория')

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'level'

    objects = TreeManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base_ppr:category', args=[self.slug])

mptt.register(Category)

@python_2_unicode_compatible
class Action(models.Model):
    """
    Описание модели
    """
    category = TreeForeignKey(Category, verbose_name=_('Category'), related_name=u'entries',)
    user_name = models.ForeignKey(User, related_name='+', to_field=u'username')
    title = models.CharField(_('Action title'), max_length=255)
    priority = models.IntegerField(verbose_name=_('Priory'))
    description = models.TextField(_('Description'), max_length=255)
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True, db_index=True)
    is_discountable = models.BooleanField(_("Is discountable?"), default=True, )

    class Meta:
        ordering = ['-date_created']
        verbose_name = _(u'')
        verbose_name_plural = _(u'Активность')

    def __str__(self):
        if self.title:
            return self.title

    def get_absolute_url(self):
        return reverse('base_ppr:item_detail', args=[str(self.pk)])

    objects = models.Manager()

@python_2_unicode_compatible
class ActionHistory(models.Model):
    """
    Описание модели
    """
    action = models.ForeignKey(Action, verbose_name=_('Action'), related_name=u'entries',)
    user_name = models.ForeignKey(User, related_name='+', to_field=u'username')
    title = models.CharField(_('Actionhistory title'), max_length=255)
    description = models.TextField(_('Description'), max_length=255)
    comment = models.TextField(_('Comment'), max_length=255)
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True, db_index=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = _(u'')
        verbose_name_plural = _(u'История')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        if self.title:
            return self.title

    def get_absolute_url(self):
        return reverse('base_ppr:item_detail', args=[str(self.pk)])

    objects = models.Manager()
