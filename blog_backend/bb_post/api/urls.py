from django.conf.urls import patterns, url

from .views import post, comments


urlpatterns = patterns('',
    url(r'^$', post.Collection.as_view()),
    url(r'^/(?P<post_id>\d+)$', post.Single.as_view()),
    url(r'^/comments', comments.Collection.as_view()),
)
