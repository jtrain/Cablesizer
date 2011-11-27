from django.conf.urls.defaults import *

urlpatterns = patterns('sizer.views', 
    (r'^$', 'main', {'template_name':'ampacity'}),
    (r'^ampacity/', 'main', {'template_name':'ampacity'}),
    (r'^voltdrop/', 'main', {'template_name':'voltdrop'}),
    (r'^sctemprise/', 'main', {'template_name':'sctemprise'}),
    (r'^report/', 'report'),
)
