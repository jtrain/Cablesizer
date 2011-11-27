from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    (r'^$', 'myproject.common.views.index'),
    (r'^new/', 'myproject.common.views.new'),
    (r'^disclaimer/', 'myproject.common.views.disclaimer'),
    (r'^about/', 'myproject.common.views.about'),
    
    #(r'^upgrade/', 'myproject.common.views.upgrade'),
    #(r'^feedback/', 'myproject.common.views.feedback'),
    
    (r'^iec/', include('myproject.sizer.urls')),
    (r'^nec/', include('myproject.nec.urls')),
    (r'^help/', include('myproject.help.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
