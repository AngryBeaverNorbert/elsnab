from django.conf.urls import url

from .views import (ServiceView,
                    SingleServiceView,
                    InstallationView,
                    MontageView)

app_name = 'services'
urlpatterns = [
    url(r'^$', ServiceView.as_view(), name='service'),
    url(r'^single-service/$', SingleServiceView.as_view(), name='single-service'),
    url(r'installation/$', InstallationView.as_view(), name='installation'),
    url(r'^single-installation/$', SingleServiceView.as_view(), name='single-installation'),
    url(r'^montage/$', MontageView.as_view(), name='montage'),
    url(r'^single-montage/$', SingleServiceView.as_view(), name='single-montage'),
]

