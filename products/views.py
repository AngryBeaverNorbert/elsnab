from django.views.generic import TemplateView

from .models import (
    Panels,
    Stabilizers,
    Ups,
    Genset,
    GensetDiesel,
    GensetBenzine,
    GensetGas,
    GensetWelding,
    GensetAdditionalEquipment
)


class PanelsView(TemplateView):
    template_name = 'products/single-panels.html'

    def get_context_data(self, **kwargs):
        context = super(PanelsView, self).get_context_data()
        context['panel'] = Panels.objects.filter(active=True).first()
        return context


class StabilizersView(TemplateView):
    template_name = 'products/single-stabilizers.html'

    def get_context_data(self, **kwargs):
        context = super(StabilizersView, self).get_context_data()
        context['stabilizer'] = Stabilizers.objects.filter(active=True).first()
        return context


class UpsView(TemplateView):
    template_name = 'products/single-ups.html'

    def get_context_data(self, **kwargs):
        context = super(UpsView, self).get_context_data()
        context['ups'] = Ups.objects.filter(active=True).first()
        return context


class GensetListView(TemplateView):
    template_name = 'products/genset.html'

    def get_context_data(self, **kwargs):
        context = super(GensetListView, self).get_context_data()
        context['genset'] = Genset.objects.all().first()
        context['genset_qty'] = Genset.objects.all().count()
        return context


class GensetBenzineView(TemplateView):
    template_name = 'products/single-genset-benzine.html'

    def get_context_data(self, **kwargs):
        context = super(GensetBenzineView, self).get_context_data()
        context['genset_benzine'] = GensetBenzine.objects.filter(active=True).first()
        return context


class GensetDieselView(TemplateView):
    template_name = 'products/single-genset-diesel.html'

    def get_context_data(self, **kwargs):
        context = super(GensetDieselView, self).get_context_data()
        context['genset_diesel'] = GensetDiesel.objects.filter(active=True).first()
        return context


class GensetGasView(TemplateView):
    template_name = 'products/single-genset-gas.html'

    def get_context_data(self, **kwargs):
        context = super(GensetGasView, self).get_context_data()
        context['genset_gas'] = GensetGas.objects.filter(active=True).first()
        return context


class GensetWeldingView(TemplateView):
    template_name = 'products/single-genset-welding.html'

    def get_context_data(self, **kwargs):
        context = super(GensetWeldingView, self).get_context_data()
        context['genset_welding'] = GensetWelding.objects.filter(active=True).first()
        return context


class GensetAdditionalEquipmentView(TemplateView):
    template_name = 'products/single-genset-additional-equipment.html'

    def get_context_data(self, **kwargs):
        context = super(GensetAdditionalEquipmentView, self).get_context_data()
        context['genset_additional'] = GensetAdditionalEquipment.objects.filter(active=True).first()
        return context
