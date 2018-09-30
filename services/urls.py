from django.conf.urls import url

from .views import (
    ServiceView,
    MontageView,
    InstallationView,
    SingleServiceView,
    SingleMontageView,
    SingleInstallationView
)

app_name = 'services'
urlpatterns = [
    url(r'service/$', ServiceView.as_view(), name='service'),
    url(r'^single-service/(?P<pk>\d+)$', SingleServiceView.as_view(), name='single-service'),
    url(r'installation/$', InstallationView.as_view(), name='installation'),
    url(r'^single-installation/(?P<pk>\d+)$', SingleInstallationView.as_view(), name='single-installation'),
    url(r'^montage/$', MontageView.as_view(), name='montage'),
    url(r'^single-montage/(?P<pk>\d+)$', SingleMontageView.as_view(), name='single-montage'),
]

