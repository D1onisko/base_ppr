# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django import template
from django.db.models import Count

from src.apps.effect_log.models import Category
import mptt

register = template.Library()

@register.inclusion_tag('apps/effect_log/inclusion/categories_list.html')

def menu_tag():

        categ = Category.objects.all()

        return {'categories': categ }

