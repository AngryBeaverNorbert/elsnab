from django.conf.urls import url
from .views import (BlogListView,
                    SingleBlogPostView)


app_name = 'blog'
urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='blog_list'),
    url(r'blog-post/$', SingleBlogPostView.as_view(), name='blog_post')
]
