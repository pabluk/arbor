from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'arbor.views.home', name='home'),
    # url(r'^arbor/', include('arbor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'arbor.views.home', name='home'),
    url(r'^tree/(?P<id>\d+)/$', 'arbor.views.tree', name='tree'),
    url(r'^tree/(?P<id>\d+)/vote/$', 'arbor.views.vote', name='vote'),
    url(r'^tree/(?P<tree_id>\d+)/vote/(?P<name_id>\d+)/$', 'arbor.views.results', name='results'),
    url(r'^kml/$', 'arbor.views.export', name='export'),

    url(r'^apropos/$', 'arbor.views.about', name='about'),
    url(r'^aide/$', 'arbor.views.help', name='help'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
