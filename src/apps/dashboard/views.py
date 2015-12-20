# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, BaseFormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from src.apps.effect_log.models import EffectLog
from src.apps.dashboard.forms import EffectLogForm

"""
Index page Dashboard
"""
class DashboardIndexView(TemplateView):
    template_name = 'apps/dashboard/profile.html'
    model = EffectLog

    # Для вывода обьявлений определенного юзера
    def get(self, request, *args, **kwargs):
        kwargs['object_list'] = EffectLog.objects.filter(user_name_id=request.user)
        return super(DashboardIndexView, self).get(request, *args, **kwargs)


class EffectLogWrite(CreateView):
    template_name = 'apps/dashboard/add_log.html'
    model = EffectLog
    form_class = EffectLogForm

    def form_valid(self, form):
        form = EffectLogForm(self.request.POST, self.request.FILES)
        add = form.save(commit=False)
        add.user_name_id = self.request.user
        add.save()
        return redirect('dashboard:dashboard_index')



