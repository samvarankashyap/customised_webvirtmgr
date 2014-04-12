from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^ipaddress/$', 'ipres.views.ipaddress', name='ipaddress'),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
