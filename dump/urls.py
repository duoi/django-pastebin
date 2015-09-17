from django.conf.urls import include, url, patterns
from . import views
from .models import Post

urlpatterns = [
    url(r'^$', views.new_post, name='new_post'),
    url(r'^(?P<unique_key>[a-zA-Z0-9]+)/$', 'dump.views.post_detail', name='post_detail'),
]
