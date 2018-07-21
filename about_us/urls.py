from django.conf.urls import url
from .views import AboutUsPageView

app_name = 'about_us'
urlpatterns = [
    url(r'^$', AboutUsPageView.as_view(), name='about_us')
]
