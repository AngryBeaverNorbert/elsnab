from django.views.generic import TemplateView, DetailView

from .models import (
    Services,
    SingleService,
    Montages,
    SingleMontage,
    Installations,
    SingleInstallation
)


class ServiceView(TemplateView):
    template_name = 'services/service.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceView, self).get_context_data()
        context['service'] = Services.objects.filter(active=True).first()
        context['services'] = SingleService.objects.all().filter(active=True)
        return context


class SingleServiceView(DetailView):
    model = SingleService
    template_name = 'services/single-service.html'
    context_object_name = 'service'


class InstallationView(TemplateView):
    template_name = 'services/installation.html'

    def get_context_data(self, **kwargs):
        context = super(InstallationView, self).get_context_data()
        context['installation'] = Installations.objects.filter(active=True).first()
        context['installations'] = SingleInstallation.objects.all().filter(active=True)
        return context


class SingleInstallationView(DetailView):
    model = SingleInstallation
    template_name = 'services/single-installation.html'
    context_object_name = 'installation'


class MontageView(TemplateView):
    template_name = 'services/montage.html'

    def get_context_data(self, **kwargs):
        context = super(MontageView, self).get_context_data()
        context['montage'] = Montages.objects.filter(active=True).first()
        context['montages'] = SingleMontage.objects.all().filter(active=True)
        return context


class SingleMontageView(DetailView):
    model = SingleMontage
    template_name = 'services/single-montage.html'
    context_object_name = 'montage'
