# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class NecAmpacity(models.Model):
    id = models.IntegerField(primary_key=True)
    metric_size = models.FloatField(null=True, blank=True)
    size = models.CharField(max_length=30, blank=True)
    installation = models.CharField(max_length=135, blank=True)
    cond = models.CharField(max_length=135, blank=True)
    cond_temp = models.IntegerField(null=True, blank=True)
    ampacity = models.IntegerField(null=True, blank=True)
    reference = models.CharField(max_length=180, blank=True)
    class Meta:
        db_table = u'nec_ampacity'

class NecImpedance(models.Model):
    id = models.IntegerField(primary_key=True)
    metric_size = models.FloatField(null=True, blank=True)
    size = models.CharField(max_length=30, blank=True)
    cond = models.CharField(max_length=45, blank=True)
    r = models.FloatField(null=True, blank=True)
    x = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'nec_impedance'
