from django.views.generic import TemplateView, DetailView
from .models import SingleBlog


class BlogHomeView(TemplateView):
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data()
        context['posts'] = SingleBlog.objects.all().filter(active=True)
        return context


class SingleBlogView(DetailView):
    model = SingleBlog
    template_name = 'blog/single-post.html'
    context_object_name = 'post'
