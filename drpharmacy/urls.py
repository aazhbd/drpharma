from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from drpharmacy import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drpharmacy.views.home', name='home'),
    # url(r'^drpharmacy/', include('drpharmacy.foo.urls')),

    url(r'^$', 'drpharmacy.views.home', name='home'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 'django.contrib.staticfiles.views.serve'),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), 'django.views.static.serve', kwargs=dict(document_root=settings.MEDIA_ROOT)),
)
