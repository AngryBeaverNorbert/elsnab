from django.conf.urls import url
from .views import (
    BlogHomeView,
    SingleBlogView)


app_name = 'blog'
urlpatterns = [
    url(r'^$', BlogHomeView.as_view(), name='blog_list'),
    url(r'blog-post/(?P<pk>\d+)$', SingleBlogView.as_view(), name='blog_post')
]
