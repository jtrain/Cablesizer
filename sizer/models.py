# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from django import forms

class Acresistances(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    size = models.FloatField(null=True, db_column='Size', blank=True) # Field name made lowercase.
    nocores = models.CharField(max_length=135, db_column='NoCores', blank=True) # Field name made lowercase.
    conductor = models.CharField(max_length=135, db_column='Conductor', blank=True) # Field name made lowercase.
    condtype = models.CharField(max_length=135, db_column='CondType', blank=True) # Field name made lowercase.
    temperature = models.IntegerField(null=True, db_column='Temperature', blank=True) # Field name made lowercase.
    resistance = models.FloatField(null=True, db_column='Resistance', blank=True) # Field name made lowercase.
    reference = models.CharField(max_length=180, db_column='Reference', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'acresistances'
    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.size, self.nocores, self.conductor, self.condtype, self.temperature)

class CableData(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    user = models.CharField(max_length=135, db_column='User', blank=True) # Field name made lowercase.
    cable_tag = models.CharField(max_length=135, db_column='Cable_Tag', blank=True) # Field name made lowercase.
    nocores = models.CharField(max_length=135, db_column='NoCores', blank=True) # Field name made lowercase.
    size = models.CharField(max_length=135, db_column='Size', blank=True) # Field name made lowercase.
    noparallel = models.IntegerField(null=True, db_column='NoParallel', blank=True) # Field name made lowercase.
    cable_length = models.FloatField(null=True, db_column='Cable_Length', blank=True) # Field name made lowercase.
    source = models.CharField(max_length=300, db_column='Source', blank=True) # Field name made lowercase.
    destination = models.CharField(max_length=300, db_column='Destination', blank=True) # Field name made lowercase.
    conductor = models.CharField(max_length=135, db_column='Conductor', blank=True) # Field name made lowercase.
    condshape = models.CharField(max_length=135, db_column='CondShape', blank=True) # Field name made lowercase.
    condtype = models.CharField(max_length=135, db_column='CondType', blank=True) # Field name made lowercase.
    condtemp = models.IntegerField(null=True, db_column='CondTemp', blank=True) # Field name made lowercase.
    insulation = models.CharField(max_length=135, db_column='Insulation', blank=True) # Field name made lowercase.
    protection = models.CharField(max_length=135, db_column='Protection', blank=True) # Field name made lowercase.
    prot_rating = models.FloatField(null=True, db_column='Prot_Rating', blank=True) # Field name made lowercase.
    earth_fault = models.CharField(max_length=1, db_column='Earth_Fault', blank=True) # Field name made lowercase.
    loadtype = models.CharField(max_length=135, db_column='LoadType', blank=True) # Field name made lowercase.
    nophases = models.CharField(max_length=135, db_column='NoPhases', blank=True) # Field name made lowercase.
    voltage = models.CharField(max_length=135, db_column='Voltage', blank=True) # Field name made lowercase.
    standard_motor_code = models.CharField(max_length=135, db_column='Standard_Motor_Code', blank=True) # Field name made lowercase.
    duty = models.CharField(max_length=135, db_column='Duty', blank=True) # Field name made lowercase.
    loadcurrent = models.CharField(max_length=135, db_column='LoadCurrent', blank=True) # Field name made lowercase.
    loadpower = models.CharField(max_length=135, db_column='LoadPower', blank=True) # Field name made lowercase.
    pf = models.FloatField(null=True, db_column='PF', blank=True) # Field name made lowercase.
    efficiency = models.FloatField(null=True, db_column='Efficiency', blank=True) # Field name made lowercase.
    lrc_ratio = models.FloatField(null=True, db_column='LRC_Ratio', blank=True) # Field name made lowercase.
    spf = models.FloatField(null=True, db_column='SPF', blank=True) # Field name made lowercase.
    maxvoltdrop_steady = models.FloatField(null=True, db_column='MaxVoltDrop_Steady', blank=True) # Field name made lowercase.
    maxvoltdrop_transient = models.FloatField(null=True, db_column='MaxVoltdrop_Transient', blank=True) # Field name made lowercase.
    maxfaultcurrent = models.FloatField(null=True, db_column='MaxFaultCurrent', blank=True) # Field name made lowercase.
    maxfaultduration = models.FloatField(null=True, db_column='MaxFaultDuration', blank=True) # Field name made lowercase.
    initcondtemp = models.IntegerField(null=True, db_column='InitCondTemp', blank=True) # Field name made lowercase.
    finalcondtemp = models.IntegerField(null=True, db_column='FinalCondTemp', blank=True) # Field name made lowercase.
    ef_disconnect_amps = models.FloatField(null=True, db_column='EF_Disconnect_Amps', blank=True) # Field name made lowercase.
    ambienttemp = models.IntegerField(null=True, db_column='AmbientTemp', blank=True) # Field name made lowercase.
    soiltemp = models.IntegerField(null=True, db_column='SoilTemp', blank=True) # Field name made lowercase.
    installation = models.CharField(max_length=300, db_column='Installation', blank=True) # Field name made lowercase.
    arrangement = models.CharField(max_length=300, db_column='Arrangement', blank=True) # Field name made lowercase.
    depth = models.FloatField(null=True, db_column='Depth', blank=True) # Field name made lowercase.
    thermalresistivity = models.FloatField(null=True, db_column='ThermalResistivity', blank=True) # Field name made lowercase.
    notiers = models.IntegerField(null=True, db_column='NoTiers', blank=True) # Field name made lowercase.
    nocircuits = models.IntegerField(null=True, db_column='NoCircuits', blank=True) # Field name made lowercase.
    ug_spacing = models.FloatField(null=True, db_column='UG_Spacing', blank=True) # Field name made lowercase.
    trefoil = models.CharField(max_length=1, db_column='Trefoil', blank=True) # Field name made lowercase.
    underground = models.CharField(max_length=1, db_column='Underground', blank=True) # Field name made lowercase.
    earthcond = models.CharField(max_length=135, db_column='EarthCond', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'cable_data'
    def __str__(self):
        return self.id

class EmailList(models.Model):
    idemail_list = models.IntegerField(primary_key=True)
    email_address = models.TextField(blank=True)
    date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'email_list'
        
class IecAmpacity(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    size = models.FloatField(null=True, db_column='Size', blank=True) # Field name made lowercase.
    insulation = models.CharField(max_length=45, db_column='Insulation', blank=True) # Field name made lowercase.
    material = models.CharField(max_length=60, db_column='Material', blank=True) # Field name made lowercase.
    no_cond = models.IntegerField(null=True, db_column='No_Cond', blank=True) # Field name made lowercase.
    ref_method = models.CharField(max_length=15, db_column='Ref_Method', blank=True) # Field name made lowercase.
    arrangement = models.CharField(max_length=60, db_column='Arrangement', blank=True) # Field name made lowercase.
    ampacity = models.FloatField(null=True, db_column='Ampacity', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'iec_ampacity'
    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.size, self.insulation, self.material, self.no_cond, self.ref_method)

class IecDerating(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    type = models.CharField(max_length=270, db_column='Type', blank=True) # Field name made lowercase.
    arg1 = models.CharField(max_length=60, db_column='Arg1', blank=True) # Field name made lowercase.
    arg2 = models.CharField(max_length=60, db_column='Arg2', blank=True) # Field name made lowercase.
    arg3 = models.CharField(max_length=60, db_column='Arg3', blank=True) # Field name made lowercase.
    derating = models.FloatField(null=True, db_column='Derating', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'iec_derating'
    def __str__(self):
        return '%s, %s, %s, %s' % (self.type, self.arg1, self.arg2, self.arg3)
		
class Dcresistances(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    size = models.FloatField(null=True, db_column='Size', blank=True) # Field name made lowercase.
    nocores = models.CharField(max_length=135, db_column='NoCores', blank=True) # Field name made lowercase.
    conductor = models.CharField(max_length=135, db_column='Conductor', blank=True) # Field name made lowercase.
    condtype = models.CharField(max_length=135, db_column='CondType', blank=True) # Field name made lowercase.
    resistance = models.FloatField(null=True, db_column='Resistance', blank=True) # Field name made lowercase.
    reference = models.CharField(max_length=180, db_column='Reference', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dcresistances'

class EarthConductors(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    activesize = models.CharField(max_length=135, db_column='ActiveSize', blank=True) # Field name made lowercase.
    activecond = models.CharField(max_length=135, db_column='ActiveCond', blank=True) # Field name made lowercase.
    earthsize = models.CharField(max_length=135, db_column='EarthSize', blank=True) # Field name made lowercase.
    reference = models.CharField(max_length=180, db_column='Reference', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'earth_conductors'

class Reactances(models.Model):
    size = models.FloatField(null=True, db_column='Size', blank=True) # Field name made lowercase.
    cores = models.CharField(max_length=135, db_column='Cores', blank=True) # Field name made lowercase.
    insulation = models.CharField(max_length=135, db_column='Insulation', blank=True) # Field name made lowercase.
    type = models.CharField(max_length=135, db_column='Type', blank=True) # Field name made lowercase.
    reactance = models.FloatField(null=True, db_column='Reactance', blank=True) # Field name made lowercase.
    reference = models.CharField(max_length=180, db_column='Reference', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'reactances'
    def __str__(self):
        return '%s, %s, %s, %s' % (self.size, self.cores, self.insulation, self.type)

class StandardMotors(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    rated_kw = models.FloatField(null=True, db_column='Rated_kw', blank=True) # Field name made lowercase.
    poles = models.IntegerField(null=True, db_column='Poles', blank=True) # Field name made lowercase.
    efficiency = models.FloatField(null=True, db_column='Efficiency', blank=True) # Field name made lowercase.
    pf = models.FloatField(null=True, db_column='PF', blank=True) # Field name made lowercase.
    voltage = models.FloatField(null=True, db_column='Voltage', blank=True) # Field name made lowercase.
    spf = models.FloatField(null=True, db_column='SPF', blank=True) # Field name made lowercase.
    flc = models.FloatField(null=True, db_column='FLC', blank=True) # Field name made lowercase.
    lrc = models.FloatField(null=True, db_column='LRC', blank=True) # Field name made lowercase.
    reference = models.CharField(max_length=180, db_column='Reference', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'standard_motors'