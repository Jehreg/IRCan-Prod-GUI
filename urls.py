from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mgmt.views',
    url(r'^$', 'main', name="home"),
)

urlpatterns += patterns('',
    # Example:
    # (r'^vpn_appliance/', include('vpn_appliance.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {"next_page": '/'}, name="logout"),
)

if settings.DEBUG:
    # During development make Django serve static files.
    # WARNING: this is really inefficient and should not be used for
    # production. Static files are recommended to be served by the HTTP server
    # directly.
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )
