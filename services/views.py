from django.views.generic import TemplateView


class ServiceView(TemplateView):
    template_name = 'services/service.html'


class SingleServiceView(TemplateView):
    template_name = 'services/single-service.html'


class InstallationView(TemplateView):
    template_name = 'services/installation.html'


class MontageView(TemplateView):
    template_name = 'services/montage.html'
