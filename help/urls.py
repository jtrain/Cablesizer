from django.conf.urls.defaults import *

urlpatterns = patterns('help.views', 
    (r'^$', 'help'),
    (r'^getting_started/', 'get_started'),
    (r'^principles/', 'principles'),
    (r'^nec_tutorial/', 'nec_tutorial'),
    (r'^iec_tutorial/', 'iec_tutorial'),
    (r'^nec_cabletypes/', 'nec_cabletypes'),
    (r'^iec_refmethods/', 'iec_refmethods'),
    (r'^tech_notes/', 'tech_notes'),
    (r'^troubleshooting/', 'troubleshooting'),
)
