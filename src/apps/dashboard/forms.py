# -*- coding: utf-8 -*-
from django.forms import ModelForm, ModelChoiceField
from django import forms
from itertools import groupby
from operator import attrgetter
import mptt

from src.apps.effect_log.models import EffectLog, Category


class SelectCategory(ModelChoiceField):
    def __init__(self, *args, **kwargs):
        super(SelectCategory, self).__init__(*args, **kwargs)

        # фильтрация по полю 'description'.для внесение новых пунктов требуется перезапустить сервер
        groups = groupby(kwargs['queryset'], attrgetter('description'))

        self.choices = [(continent, [(c.id, self.label_from_instance(c)) for c in countries])
                        for continent, countries in groups]


class BaseFields(forms.Form):

    category = SelectCategory(queryset=Category.objects.exclude(level=0),
                              label=u'Категория',)


"""
class adds products in dashboard
"""

class EffectLogForm(ModelForm, BaseFields):
    class Meta:
        model = EffectLog
        fields = 'category','operator','type_prostoy','time_prostoy','dlitelnost_prostoya','comments',

