from django.conf.urls import url

from .views import (GensetListView,
                    GensetAdditionalEquipmentView,
                    GensetBenzineView,
                    GensetDieselView,
                    GensetGasView,
                    GensetWeldingView,
                    PanelsView,
                    StabilizersView,
                    UpsView)

app_name = 'products'
urlpatterns = [
    url(r'^genset/$', GensetListView.as_view(), name='genset_list'),
    url(r'^genset/single-genset-additional-equipment/$', GensetAdditionalEquipmentView.as_view(), name='single-genset-additional-equipment'),
    url(r'^genset/single-genset-benzine/$', GensetBenzineView.as_view(), name='single-genset-benzine'),
    url(r'^genset/single-genset-diesel/$', GensetDieselView.as_view(), name='single-genset-diesel'),
    url(r'^genset/single-genset-gas/$', GensetGasView.as_view(), name='single-genset-gas'),
    url(r'^genset/single-genset-welding/$', GensetWeldingView.as_view(), name='single-genset-welding'),
    url(r'^panels/$', PanelsView.as_view(), name='panels'),
    url(r'^stabilizers/$', StabilizersView.as_view(), name='stabilizers'),
    url(r'^ups/$', UpsView.as_view(), name='ups'),
]
