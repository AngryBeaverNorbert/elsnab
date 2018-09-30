# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from .models import Home


class HomePageView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data()
        context['home_view'] = Home.objects.filter(active=True).first()
        return context
