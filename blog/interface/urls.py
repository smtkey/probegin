from django.conf.urls import patterns, include, url

from django.contrib.auth import views as auth_views
from .views import post, signup


urlpatterns = patterns('',
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^signup/$', signup.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        signup.activate, name='activate'),
    url('^post', include(patterns('',
        url(r'^$', post.List.as_view(), name='list'),
        url(r'^/(?P<post_id>\d+)$', post.View.as_view(), name='view'),
    ), namespace='post')),
)
