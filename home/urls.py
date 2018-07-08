from django.conf.urls import url
from django.views.generic import TemplateView
# from .views import MainPageView

app_name = 'home'
urlpatterns = [
    url(r'', TemplateView.as_view(template_name='home/home.html'), name='home'),
    # url(r'left/', TemplateView.as_view(template_name='left-sidebar.html'), name='left'),
    # url(r'right/', TemplateView.as_view(template_name='right-sidebar.html'), name='right'),
    # url(r'elements/', TemplateView.as_view(template_name='contact.html'), name='elements'),
    # url(r'contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]