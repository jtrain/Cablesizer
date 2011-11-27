from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render_to_response
from datetime import datetime

# Help index page
def help(request):
    return render_to_response("help.html")

def get_started(request):
    return render_to_response("get_started.html")

def principles(request):
    return render_to_response("principles.html")
    
def nec_tutorial(request):
    return render_to_response("nec_tutorial.html")
    
def iec_tutorial(request):
    return render_to_response("iec_tutorial.html")

def nec_cabletypes(request):
    return render_to_response("nec_cabletypes.html")

def iec_refmethods(request):
    return render_to_response("iec_refmethods.html")

def tech_notes(request):
    return render_to_response("technotes.html")
    
# Troubleshooting page
def troubleshooting(request):  
    return render_to_response('faq.html')
