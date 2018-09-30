from django.contrib import admin
from .models import (
    # Blog,
    SingleBlog,
    BlogImage
)


class SingleBlogImageInline(admin.TabularInline):
    model = BlogImage


class SingleBlogAdmin(admin.ModelAdmin):
    inlines = [
        SingleBlogImageInline
    ]


# admin.site.register(Blog)
admin.site.register(SingleBlog, SingleBlogAdmin)
