from django.conf.urls import url
from .views import ContactsView

app_name = 'contacts'
urlpatterns = [
    url(r'^$', ContactsView.as_view(), name='contacts')
]
