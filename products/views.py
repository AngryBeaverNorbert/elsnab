from django.views.generic import TemplateView


class PanelsView(TemplateView):
    template_name = 'products/single-panels.html'


class StabilizersView(TemplateView):
    template_name = 'products/single-stabilizers.html'


class UpsView(TemplateView):
    template_name = 'products/single-ups.html'


class GensetListView(TemplateView):
    template_name = 'products/genset.html'


class GensetAdditionalEquipmentView(TemplateView):
    template_name = 'products/single-genset-additional-equipment.html'


class GensetBenzineView(TemplateView):
    template_name = 'products/single-genset-benzine.html'


class GensetDieselView(TemplateView):
    template_name = 'products/single-genset-diesel.html'


class GensetGasView(TemplateView):
    template_name = 'products/single-genset-gas.html'


class GensetWeldingView(TemplateView):
    template_name = 'products/single-genset-welding.html'
