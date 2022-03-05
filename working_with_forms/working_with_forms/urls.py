from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import path

from form_without_model.views import contact_us_view
from working_with_modelform.views import (
    create_blog_view, 
    get_blog_posts_list_view,
    get_detailed_blog_post
)


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('form-without-model/', contact_us_view),
    path('posts/home/', get_blog_posts_list_view, name='list-posts'),
    path('posts/create/', create_blog_view, name='create-post'),
    path('posts/<int:id>/', get_detailed_blog_post, name='detail-post')
]
