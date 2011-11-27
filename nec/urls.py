from django.conf.urls.defaults import *

urlpatterns = patterns('nec.views', 
    (r'^$', 'main', {'template_name':'ampacity'}),
    (r'^ampacity/', 'main', {'template_name':'ampacity'}),
    (r'^voltdrop/', 'main', {'template_name':'voltdrop'}),
    (r'^report/', 'report'),
)
