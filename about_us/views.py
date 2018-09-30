# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from .models import AboutUs


class AboutUsPageView(TemplateView):
    template_name = 'about_us/about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsPageView, self).get_context_data()
        context['about_us'] = AboutUs.objects.filter(active=True).first()
        return context
