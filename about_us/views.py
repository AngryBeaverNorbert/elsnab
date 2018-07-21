from django.views.generic import TemplateView


class AboutUsPageView(TemplateView):
    template_name = 'about_us/about_us.html'
