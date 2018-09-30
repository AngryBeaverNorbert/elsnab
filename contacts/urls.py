from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ContactsView

app_name = 'contacts'
urlpatterns = [
    url(r'^$', ContactsView.as_view(), name='contacts'),
    url(r'^mail-sent/$', TemplateView.as_view(template_name='contacts/sent-mail.html'), name='mail-sent')
]
