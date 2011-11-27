# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

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

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=240)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(unique=True, max_length=300)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=90)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

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

class CurrentRatingsMulti(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    size = models.FloatField(null=True, db_column='Size', blank=True) # Field name made lowercase.
    nocores = models.CharField(max_length=135, db_column='NoCores', blank=True) # Field name made lowercase.
    insulation = models.CharField(max_length=135, db_column='Insulation', blank=True) # Field name made lowercase.
    conductor = models.CharField(max_length=135, db_column='Conductor', blank=True) # Field name made lowercase.
    condtemp = models.IntegerField(null=True, db_column='CondTemp', blank=True) # Field name made lowercase.
    installation = models.CharField(max_length=300, db_column='Installation', blank=True) # Field name made lowercase.
    currentrating = models.FloatField(null=True, db_column='CurrentRating', blank=True) # Field name made lowercase.
    reference = models.CharField(max_length=135, db_column='Reference', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'current_ratings_multi'

class CurrentRatingsSingle(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    size = models.FloatField(null=True, db_column='Size', blank=True) # Field name made lowercase.
    nocores = models.CharField(max_length=135, db_column='NoCores', blank=True) # Field name made lowercase.
    insulation = models.CharField(max_length=135, db_column='Insulation', blank=True) # Field name made lowercase.
    conductor = models.CharField(max_length=135, db_column='Conductor', blank=True) # Field name made lowercase.
    condtemp = models.IntegerField(null=True, db_column='CondTemp', blank=True) # Field name made lowercase.
    installation = models.CharField(max_length=300, db_column='Installation', blank=True) # Field name made lowercase.
    currentrating = models.IntegerField(null=True, db_column='CurrentRating', blank=True) # Field name made lowercase.
    reference = models.CharField(max_length=180, db_column='Reference', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'current_ratings_single'

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

class Deratings(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    factor = models.CharField(max_length=135, db_column='Factor', blank=True) # Field name made lowercase.
    arg1 = models.CharField(max_length=135, db_column='Arg1', blank=True) # Field name made lowercase.
    arg2 = models.CharField(max_length=180, db_column='Arg2', blank=True) # Field name made lowercase.
    arg3 = models.CharField(max_length=135, db_column='Arg3', blank=True) # Field name made lowercase.
    arg4 = models.CharField(max_length=135, db_column='Arg4', blank=True) # Field name made lowercase.
    arg5 = models.CharField(max_length=135, db_column='Arg5', blank=True) # Field name made lowercase.
    derating = models.FloatField(null=True, db_column='Derating', blank=True) # Field name made lowercase.
    reference = models.CharField(max_length=180, db_column='Reference', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'deratings'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(unique=True, max_length=300)
    model = models.CharField(unique=True, max_length=300)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class EarthConductors(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    activesize = models.CharField(max_length=135, db_column='ActiveSize', blank=True) # Field name made lowercase.
    activecond = models.CharField(max_length=135, db_column='ActiveCond', blank=True) # Field name made lowercase.
    earthsize = models.CharField(max_length=135, db_column='EarthSize', blank=True) # Field name made lowercase.
    reference = models.CharField(max_length=180, db_column='Reference', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'earth_conductors'

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

class IecDerating(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    type = models.CharField(max_length=270, db_column='Type', blank=True) # Field name made lowercase.
    arg1 = models.CharField(max_length=60, db_column='Arg1', blank=True) # Field name made lowercase.
    arg2 = models.CharField(max_length=60, db_column='Arg2', blank=True) # Field name made lowercase.
    arg3 = models.CharField(max_length=60, db_column='Arg3', blank=True) # Field name made lowercase.
    derating = models.FloatField(null=True, db_column='Derating', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'iec_derating'

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

class ScConstant(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    inittemp = models.IntegerField(null=True, db_column='InitTemp', blank=True) # Field name made lowercase.
    finaltemp = models.IntegerField(null=True, db_column='FinalTemp', blank=True) # Field name made lowercase.
    material = models.CharField(max_length=135, db_column='Material', blank=True) # Field name made lowercase.
    constantk = models.FloatField(null=True, db_column='ConstantK', blank=True) # Field name made lowercase.
    reference = models.CharField(max_length=180, db_column='Reference', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'sc_constant'

class StandardMotors(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    rated_kw = models.CharField(max_length=30, db_column='Rated_kw', blank=True) # Field name made lowercase.
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

