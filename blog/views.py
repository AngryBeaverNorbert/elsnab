from django.views.generic import TemplateView, DetailView


class BlogListView(TemplateView):
    template_name = 'blog/blog.html'


class SingleBlogPostView(TemplateView):
    template_name = 'blog/single-post.html'
