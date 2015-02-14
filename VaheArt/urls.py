from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import home

urlpatterns = patterns('',
    url(r'^$', 'home.views.home', name='home'),
    url(r'^ajax/galery/$', 'home.views.galeryJson', name='galery'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
