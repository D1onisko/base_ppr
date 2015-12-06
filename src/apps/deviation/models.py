# -*- coding: utf-8 -*-
import os
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class Deviation(models.Model):
    """
    Журнал отклонений
    """
    user_name = models.ForeignKey(User, related_name='+', to_field=u"username")
    description = models.TextField(verbose_name="Description", blank=True)
    date_created = models.DateTimeField(verbose_name="Date created", auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def get_absolute_url(self):
        return reverse('base_ppr:plan_detail', args=[str(self.pk)])
