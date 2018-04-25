# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BuildingFootprints(models.Model):
    objectid = models.AutoField(primary_key=True)
    bfid = models.IntegerField(blank=True, null=True)
    categ = models.SmallIntegerField(blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'building_footprints'


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


class ElectricalTransmissionStructures(models.Model):
    objectid = models.AutoField(primary_key=True)
    poleid = models.IntegerField(blank=True, null=True)
    pole_ref = models.CharField(max_length=20, blank=True, null=True)
    csz_wet_pgd = models.SmallIntegerField(blank=True, null=True)
    csz_wet_prob = models.SmallIntegerField(blank=True, null=True)
    csz_dry_pgd = models.SmallIntegerField(blank=True, null=True)
    csz_dry_prob = models.SmallIntegerField(blank=True, null=True)
    phf_wet_pgd = models.SmallIntegerField(blank=True, null=True)
    phf_wet_prob = models.SmallIntegerField(blank=True, null=True)
    phf_dry_pgd = models.SmallIntegerField(blank=True, null=True)
    phf_dry_prob = models.SmallIntegerField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'electrical_transmission_structures'


class EmergencyTransportationRoutes(models.Model):
    objectid = models.AutoField(primary_key=True)
    segmentid = models.SmallIntegerField(blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    csz_wet_class = models.SmallIntegerField(blank=True, null=True)
    csz_dry_class = models.SmallIntegerField(blank=True, null=True)
    phf_wet_class = models.SmallIntegerField(blank=True, null=True)
    phf_dry_class = models.SmallIntegerField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'emergency_transportation_routes'


class Hydrants(models.Model):
    objectid = models.AutoField(primary_key=True)
    mainvalvetype = models.CharField(max_length=20, blank=True, null=True)
    hydrantnumber = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=3, blank=True, null=True)
    gatecrossstcmnt = models.CharField(max_length=200, blank=True, null=True)
    gatecurbstcmnt = models.CharField(max_length=200, blank=True, null=True)
    controls = models.CharField(max_length=55, blank=True, null=True)
    streetprefix = models.CharField(max_length=2, blank=True, null=True)
    gatecrossstprefix = models.CharField(max_length=2, blank=True, null=True)
    gatecurbstprefix = models.CharField(max_length=2, blank=True, null=True)
    district = models.CharField(max_length=3, blank=True, null=True)
    hydrantcrossstcmnt = models.CharField(max_length=200, blank=True, null=True)
    hydrantcurbstcmnt = models.CharField(max_length=200, blank=True, null=True)
    hydrantcrossstprefix = models.CharField(max_length=2, blank=True, null=True)
    hydrantcurbstprefix = models.CharField(max_length=2, blank=True, null=True)
    hydrantcrossstline = models.CharField(max_length=4, blank=True, null=True)
    hydrantcurbstline = models.CharField(max_length=4, blank=True, null=True)
    hydmaint = models.CharField(max_length=60, blank=True, null=True)
    hydrantmanufacturer = models.CharField(max_length=25, blank=True, null=True)
    hydrantsize = models.FloatField(blank=True, null=True)
    hydrantcrossst = models.CharField(max_length=60, blank=True, null=True)
    hydrantcurbst = models.CharField(max_length=60, blank=True, null=True)
    hydrantcrosssttype = models.CharField(max_length=6, blank=True, null=True)
    hydrantcurbsttype = models.CharField(max_length=6, blank=True, null=True)
    gatecrossstline = models.CharField(max_length=4, blank=True, null=True)
    gatecurbstline = models.CharField(max_length=4, blank=True, null=True)
    gatemanufacturer = models.CharField(max_length=25, blank=True, null=True)
    street = models.CharField(max_length=60, blank=True, null=True)
    gateopens = models.CharField(max_length=3, blank=True, null=True)
    gatecrossst = models.CharField(max_length=60, blank=True, null=True)
    gatecurbst = models.CharField(max_length=60, blank=True, null=True)
    sttype = models.CharField(max_length=6, blank=True, null=True)
    gatecrosssttype = models.CharField(max_length=6, blank=True, null=True)
    gatecurbsttype = models.CharField(max_length=6, blank=True, null=True)
    hydrantstyle = models.CharField(max_length=25, blank=True, null=True)
    watertype = models.CharField(max_length=20, blank=True, null=True)
    waterdistrict = models.CharField(max_length=40, blank=True, null=True)
    facilityid = models.FloatField(blank=True, null=True)
    recorddate = models.DateTimeField(blank=True, null=True)
    locationdetail = models.CharField(max_length=120, blank=True, null=True)
    pressuresource = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    constructiondate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=20, blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    tempident = models.FloatField(blank=True, null=True)
    synergenid = models.CharField(max_length=17, blank=True, null=True)
    annexationdate = models.DateTimeField(blank=True, null=True)
    annexed = models.CharField(max_length=3, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    researched = models.CharField(max_length=3, blank=True, null=True)
    installworkorder = models.CharField(max_length=12, blank=True, null=True)
    removaldate = models.DateTimeField(blank=True, null=True)
    fireonly = models.CharField(max_length=50, blank=True, null=True)
    dataflag = models.CharField(max_length=50, blank=True, null=True)
    manufacturerdate = models.DateTimeField(blank=True, null=True)
    av_oid = models.FloatField(blank=True, null=True)
    facility_folder = models.CharField(max_length=500, blank=True, null=True)
    projectnumber = models.CharField(max_length=20, blank=True, null=True)
    removalproject = models.CharField(max_length=20, blank=True, null=True)
    conditionranking = models.CharField(max_length=1, blank=True, null=True)
    dateconditionranked = models.DateTimeField(blank=True, null=True)
    breakawayinstalled = models.CharField(max_length=3, blank=True, null=True)
    flushingcycle = models.CharField(max_length=3, blank=True, null=True)
    flushed = models.CharField(max_length=3, blank=True, null=True)
    last_flshed = models.DateTimeField(blank=True, null=True)
    flushingreason = models.CharField(max_length=250, blank=True, null=True)
    parentassetid = models.CharField(max_length=15, blank=True, null=True)
    opspecialuse = models.CharField(max_length=3, blank=True, null=True)
    depthofmain = models.IntegerField(blank=True, null=True)
    gatecrossstdistance = models.IntegerField(blank=True, null=True)
    gatecurbstdistance = models.IntegerField(blank=True, null=True)
    hydrantcrossstdist = models.IntegerField(blank=True, null=True)
    hydrantcurbstdist = models.IntegerField(blank=True, null=True)
    gatesize = models.FloatField(blank=True, null=True)
    gatenumberofturns = models.FloatField(blank=True, null=True)
    fittingcode = models.IntegerField(blank=True, null=True)
    rotation = models.FloatField(blank=True, null=True)
    subtype = models.IntegerField(blank=True, null=True)
    quartersection = models.IntegerField(blank=True, null=True)
    owningbusparty = models.IntegerField(blank=True, null=True)
    ancillaryrole = models.IntegerField(blank=True, null=True)
    enabled = models.SmallIntegerField(blank=True, null=True)
    rotation802 = models.FloatField(blank=True, null=True)
    burydepth = models.IntegerField(blank=True, null=True)
    mainsize = models.FloatField(blank=True, null=True)
    parentassetname = models.CharField(max_length=250, blank=True, null=True)
    pwbreferencename = models.CharField(max_length=500, blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'hydrants'


class Jurisdictions(models.Model):
    objectid = models.AutoField(primary_key=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    jurisdiction = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=20, blank=True, null=True)
    acres = models.FloatField(blank=True, null=True)
    bldgcount = models.IntegerField(blank=True, null=True)
    bldgsqft = models.IntegerField(blank=True, null=True)
    bldgcost = models.FloatField(blank=True, null=True)
    bldgweight = models.IntegerField(blank=True, null=True)
    contentcost = models.FloatField(blank=True, null=True)
    permresidents = models.IntegerField(blank=True, null=True)
    dayoccupants = models.IntegerField(blank=True, null=True)
    nightoccupants = models.IntegerField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'jurisdictions'


class LossJurisdictionCszM9P0Dry(models.Model):
    objectid = models.AutoField(primary_key=True)
    jurisdiction = models.CharField(max_length=100, blank=True, null=True)
    bldgloss = models.FloatField(blank=True, null=True)
    bldg_lr = models.FloatField(blank=True, null=True)
    contentloss = models.FloatField(blank=True, null=True)
    debris = models.FloatField(blank=True, null=True)
    displacedpop = models.FloatField(blank=True, null=True)
    casdaytotal = models.FloatField(blank=True, null=True)
    casdayl1 = models.FloatField(blank=True, null=True)
    casdayl2 = models.FloatField(blank=True, null=True)
    casdayl3 = models.FloatField(blank=True, null=True)
    casdayl4 = models.FloatField(blank=True, null=True)
    casnighttotal = models.FloatField(blank=True, null=True)
    casnightl1 = models.FloatField(blank=True, null=True)
    casnightl2 = models.FloatField(blank=True, null=True)
    casnightl3 = models.FloatField(blank=True, null=True)
    casnightl4 = models.FloatField(blank=True, null=True)
    pdsnone = models.IntegerField(blank=True, null=True)
    pdsslight = models.IntegerField(blank=True, null=True)
    pdsmoderate = models.IntegerField(blank=True, null=True)
    pdsextensive = models.IntegerField(blank=True, null=True)
    pdscomplete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loss_jurisdiction_csz_m9p0_dry'


class LossJurisdictionCszM9P0Wet(models.Model):
    objectid = models.AutoField(primary_key=True)
    jurisdiction = models.CharField(max_length=100, blank=True, null=True)
    bldgloss = models.FloatField(blank=True, null=True)
    bldg_lr = models.FloatField(blank=True, null=True)
    contentloss = models.FloatField(blank=True, null=True)
    debris = models.FloatField(blank=True, null=True)
    displacedpop = models.FloatField(blank=True, null=True)
    casdaytotal = models.FloatField(blank=True, null=True)
    casdayl1 = models.FloatField(blank=True, null=True)
    casdayl2 = models.FloatField(blank=True, null=True)
    casdayl3 = models.FloatField(blank=True, null=True)
    casdayl4 = models.FloatField(blank=True, null=True)
    casnighttotal = models.FloatField(blank=True, null=True)
    casnightl1 = models.FloatField(blank=True, null=True)
    casnightl2 = models.FloatField(blank=True, null=True)
    casnightl3 = models.FloatField(blank=True, null=True)
    casnightl4 = models.FloatField(blank=True, null=True)
    pdsnone = models.IntegerField(blank=True, null=True)
    pdsslight = models.IntegerField(blank=True, null=True)
    pdsmoderate = models.IntegerField(blank=True, null=True)
    pdsextensive = models.IntegerField(blank=True, null=True)
    pdscomplete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loss_jurisdiction_csz_m9p0_wet'


class LossJurisdictionPhfM6P8Dry(models.Model):
    objectid = models.AutoField(primary_key=True)
    jurisdiction = models.CharField(max_length=100, blank=True, null=True)
    bldgloss = models.FloatField(blank=True, null=True)
    bldg_lr = models.FloatField(blank=True, null=True)
    contentloss = models.FloatField(blank=True, null=True)
    debris = models.FloatField(blank=True, null=True)
    displacedpop = models.FloatField(blank=True, null=True)
    casdaytotal = models.FloatField(blank=True, null=True)
    casdayl1 = models.FloatField(blank=True, null=True)
    casdayl2 = models.FloatField(blank=True, null=True)
    casdayl3 = models.FloatField(blank=True, null=True)
    casdayl4 = models.FloatField(blank=True, null=True)
    casnighttotal = models.FloatField(blank=True, null=True)
    casnightl1 = models.FloatField(blank=True, null=True)
    casnightl2 = models.FloatField(blank=True, null=True)
    casnightl3 = models.FloatField(blank=True, null=True)
    casnightl4 = models.FloatField(blank=True, null=True)
    pdsnone = models.IntegerField(blank=True, null=True)
    pdsslight = models.IntegerField(blank=True, null=True)
    pdsmoderate = models.IntegerField(blank=True, null=True)
    pdsextensive = models.IntegerField(blank=True, null=True)
    pdscomplete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loss_jurisdiction_phf_m6p8_dry'


class LossJurisdictionPhfM6P8Wet(models.Model):
    objectid = models.AutoField(primary_key=True)
    jurisdiction = models.CharField(max_length=100, blank=True, null=True)
    bldgloss = models.FloatField(blank=True, null=True)
    bldg_lr = models.FloatField(blank=True, null=True)
    contentloss = models.FloatField(blank=True, null=True)
    debris = models.FloatField(blank=True, null=True)
    displacedpop = models.FloatField(blank=True, null=True)
    casdaytotal = models.FloatField(blank=True, null=True)
    casdayl1 = models.FloatField(blank=True, null=True)
    casdayl2 = models.FloatField(blank=True, null=True)
    casdayl3 = models.FloatField(blank=True, null=True)
    casdayl4 = models.FloatField(blank=True, null=True)
    casnighttotal = models.FloatField(blank=True, null=True)
    casnightl1 = models.FloatField(blank=True, null=True)
    casnightl2 = models.FloatField(blank=True, null=True)
    casnightl3 = models.FloatField(blank=True, null=True)
    casnightl4 = models.FloatField(blank=True, null=True)
    pdsnone = models.IntegerField(blank=True, null=True)
    pdsslight = models.IntegerField(blank=True, null=True)
    pdsmoderate = models.IntegerField(blank=True, null=True)
    pdsextensive = models.IntegerField(blank=True, null=True)
    pdscomplete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loss_jurisdiction_phf_m6p8_wet'


class LossNeighborhoodUnitCszM9P0Dry(models.Model):
    objectid = models.AutoField(primary_key=True)
    nuid = models.SmallIntegerField(blank=True, null=True)
    bldgloss = models.FloatField(blank=True, null=True)
    bldg_lr = models.FloatField(blank=True, null=True)
    contentloss = models.IntegerField(blank=True, null=True)
    debris = models.IntegerField(blank=True, null=True)
    displacedpop = models.FloatField(blank=True, null=True)
    casdaytotal = models.FloatField(blank=True, null=True)
    casdayl1 = models.FloatField(blank=True, null=True)
    casdayl2 = models.FloatField(blank=True, null=True)
    casdayl3 = models.FloatField(blank=True, null=True)
    casdayl4 = models.FloatField(blank=True, null=True)
    casnighttotal = models.FloatField(blank=True, null=True)
    casnightl1 = models.FloatField(blank=True, null=True)
    casnightl2 = models.FloatField(blank=True, null=True)
    casnightl3 = models.FloatField(blank=True, null=True)
    casnightl4 = models.FloatField(blank=True, null=True)
    pdsnone = models.IntegerField(blank=True, null=True)
    pdsslight = models.IntegerField(blank=True, null=True)
    pdsmoderate = models.IntegerField(blank=True, null=True)
    pdsextensive = models.IntegerField(blank=True, null=True)
    pdscomplete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loss_neighborhood_unit_csz_m9p0_dry'


class LossNeighborhoodUnitCszM9P0Wet(models.Model):
    objectid = models.AutoField(primary_key=True)
    nuid = models.SmallIntegerField(blank=True, null=True)
    bldgloss = models.FloatField(blank=True, null=True)
    bldg_lr = models.FloatField(blank=True, null=True)
    contentloss = models.IntegerField(blank=True, null=True)
    debris = models.IntegerField(blank=True, null=True)
    displacedpop = models.FloatField(blank=True, null=True)
    casdaytotal = models.FloatField(blank=True, null=True)
    casdayl1 = models.FloatField(blank=True, null=True)
    casdayl2 = models.FloatField(blank=True, null=True)
    casdayl3 = models.FloatField(blank=True, null=True)
    casdayl4 = models.FloatField(blank=True, null=True)
    casnighttotal = models.FloatField(blank=True, null=True)
    casnightl1 = models.FloatField(blank=True, null=True)
    casnightl2 = models.FloatField(blank=True, null=True)
    casnightl3 = models.FloatField(blank=True, null=True)
    casnightl4 = models.FloatField(blank=True, null=True)
    pdsnone = models.IntegerField(blank=True, null=True)
    pdsslight = models.IntegerField(blank=True, null=True)
    pdsmoderate = models.IntegerField(blank=True, null=True)
    pdsextensive = models.IntegerField(blank=True, null=True)
    pdscomplete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loss_neighborhood_unit_csz_m9p0_wet'


class LossNeighborhoodUnitPhfM6P8Dry(models.Model):
    objectid = models.AutoField(primary_key=True)
    nuid = models.SmallIntegerField(blank=True, null=True)
    bldgloss = models.FloatField(blank=True, null=True)
    bldg_lr = models.FloatField(blank=True, null=True)
    contentloss = models.IntegerField(blank=True, null=True)
    debris = models.IntegerField(blank=True, null=True)
    displacedpop = models.FloatField(blank=True, null=True)
    casdaytotal = models.FloatField(blank=True, null=True)
    casdayl1 = models.FloatField(blank=True, null=True)
    casdayl2 = models.FloatField(blank=True, null=True)
    casdayl3 = models.FloatField(blank=True, null=True)
    casdayl4 = models.FloatField(blank=True, null=True)
    casnighttotal = models.FloatField(blank=True, null=True)
    casnightl1 = models.FloatField(blank=True, null=True)
    casnightl2 = models.FloatField(blank=True, null=True)
    casnightl3 = models.FloatField(blank=True, null=True)
    casnightl4 = models.FloatField(blank=True, null=True)
    pdsnone = models.IntegerField(blank=True, null=True)
    pdsslight = models.IntegerField(blank=True, null=True)
    pdsmoderate = models.IntegerField(blank=True, null=True)
    pdsextensive = models.IntegerField(blank=True, null=True)
    pdscomplete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loss_neighborhood_unit_phf_m6p8_dry'


class LossNeighborhoodUnitPhfM6P8Wet(models.Model):
    objectid = models.AutoField(primary_key=True)
    nuid = models.SmallIntegerField(blank=True, null=True)
    bldgloss = models.FloatField(blank=True, null=True)
    bldg_lr = models.FloatField(blank=True, null=True)
    contentloss = models.IntegerField(blank=True, null=True)
    debris = models.IntegerField(blank=True, null=True)
    displacedpop = models.FloatField(blank=True, null=True)
    casdaytotal = models.FloatField(blank=True, null=True)
    casdayl1 = models.FloatField(blank=True, null=True)
    casdayl2 = models.FloatField(blank=True, null=True)
    casdayl3 = models.FloatField(blank=True, null=True)
    casdayl4 = models.FloatField(blank=True, null=True)
    casnighttotal = models.FloatField(blank=True, null=True)
    casnightl1 = models.FloatField(blank=True, null=True)
    casnightl2 = models.FloatField(blank=True, null=True)
    casnightl3 = models.FloatField(blank=True, null=True)
    casnightl4 = models.FloatField(blank=True, null=True)
    pdsnone = models.IntegerField(blank=True, null=True)
    pdsslight = models.IntegerField(blank=True, null=True)
    pdsmoderate = models.IntegerField(blank=True, null=True)
    pdsextensive = models.IntegerField(blank=True, null=True)
    pdscomplete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loss_neighborhood_unit_phf_m6p8_wet'


class NeighborhoodUnits(models.Model):
    objectid = models.AutoField(primary_key=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    nuid = models.SmallIntegerField(blank=True, null=True)
    county = models.CharField(max_length=20, blank=True, null=True)
    acres = models.FloatField(blank=True, null=True)
    bldgcount = models.IntegerField(blank=True, null=True)
    bldgsqft = models.IntegerField(blank=True, null=True)
    bldgcost = models.FloatField(blank=True, null=True)
    bldgweight = models.IntegerField(blank=True, null=True)
    contentcost = models.FloatField(blank=True, null=True)
    permresidents = models.IntegerField(blank=True, null=True)
    dayoccupants = models.IntegerField(blank=True, null=True)
    nightoccupants = models.IntegerField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'neighborhood_units'


class PhfM6P8BedrockGroundmotion(models.Model):
    objectid = models.AutoField(primary_key=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    pga = models.FloatField(blank=True, null=True)
    pgv = models.FloatField(blank=True, null=True)
    sa03 = models.FloatField(blank=True, null=True)
    sa10 = models.FloatField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'phf_m6p8_bedrock_groundmotion'


class PointsOfService(models.Model):
    objectid = models.AutoField(primary_key=True)
    accountid = models.FloatField(blank=True, null=True)
    addressnumber = models.CharField(max_length=12, blank=True, null=True)
    facilityid = models.FloatField(blank=True, null=True)
    tempuid = models.FloatField(blank=True, null=True)
    commentary = models.CharField(max_length=120, blank=True, null=True)
    modifiedby = models.CharField(max_length=50, blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    annexationdate = models.DateTimeField(blank=True, null=True)
    annexed = models.CharField(max_length=3, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    researched = models.CharField(max_length=3, blank=True, null=True)
    av_oid = models.FloatField(blank=True, null=True)
    subtype = models.IntegerField(blank=True, null=True)
    enabled = models.SmallIntegerField(blank=True, null=True)
    ancillaryrole = models.SmallIntegerField(blank=True, null=True)
    location_no = models.FloatField(blank=True, null=True)
    parentassetid = models.CharField(max_length=15, blank=True, null=True)
    parentassetname = models.CharField(max_length=250, blank=True, null=True)
    pwbreferencename = models.CharField(max_length=500, blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'points_of_service'


class PopulationAndBuildingDensity(models.Model):
    objectid = models.AutoField(primary_key=True)
    bldgcount = models.SmallIntegerField(blank=True, null=True)
    permres = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    bldgcount_res = models.SmallIntegerField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'population_and_building_density'


class PressureZones(models.Model):
    objectid = models.AutoField(primary_key=True)
    zoneid = models.FloatField(blank=True, null=True)
    zonehgl = models.IntegerField(blank=True, null=True)
    zonesource = models.CharField(max_length=50, blank=True, null=True)
    zonestreet = models.CharField(max_length=50, blank=True, null=True)
    zonecomments = models.CharField(max_length=200, blank=True, null=True)
    zonename = models.CharField(max_length=120, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    deliverymethod = models.CharField(max_length=200, blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pressure_zones'


class PressurizedMains(models.Model):
    objectid = models.AutoField(primary_key=True)
    depthinches = models.IntegerField(blank=True, null=True)
    pressurerating = models.CharField(max_length=7, blank=True, null=True)
    material = models.CharField(max_length=5, blank=True, null=True)
    exteriorcoating = models.CharField(max_length=5, blank=True, null=True)
    liningtype = models.CharField(max_length=6, blank=True, null=True)
    roughness = models.IntegerField(blank=True, null=True)
    recordedlength = models.IntegerField(blank=True, null=True)
    flowmeasurementid = models.FloatField(blank=True, null=True)
    watertype = models.CharField(max_length=5, blank=True, null=True)
    quartersection = models.IntegerField(blank=True, null=True)
    owningbusparty = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    locationdetail = models.CharField(max_length=120, blank=True, null=True)
    waterdistrict = models.CharField(max_length=40, blank=True, null=True)
    facilityid = models.FloatField(blank=True, null=True)
    recorddate = models.DateTimeField(blank=True, null=True)
    pressuresource = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    subtype = models.IntegerField(blank=True, null=True)
    constructiondate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=20, blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    enabled = models.SmallIntegerField(blank=True, null=True)
    mainsize = models.FloatField(blank=True, null=True)
    specialconditions = models.CharField(max_length=40, blank=True, null=True)
    district = models.CharField(max_length=3, blank=True, null=True)
    tempident = models.FloatField(blank=True, null=True)
    fairshare = models.CharField(max_length=50, blank=True, null=True)
    flushdate = models.DateTimeField(blank=True, null=True)
    synergenid = models.CharField(max_length=17, blank=True, null=True)
    annexationdate = models.DateTimeField(blank=True, null=True)
    annexed = models.CharField(max_length=3, blank=True, null=True)
    researched = models.CharField(max_length=3, blank=True, null=True)
    installworkorder = models.CharField(max_length=12, blank=True, null=True)
    removaldate = models.DateTimeField(blank=True, null=True)
    streetname = models.CharField(max_length=250, blank=True, null=True)
    dataflag = models.CharField(max_length=3, blank=True, null=True)
    amid = models.FloatField(blank=True, null=True)
    facility_folder = models.CharField(max_length=500, blank=True, null=True)
    projectnumber = models.CharField(max_length=20, blank=True, null=True)
    removalproject = models.CharField(max_length=20, blank=True, null=True)
    estimatedinstallyear = models.CharField(max_length=4, blank=True, null=True)
    parentassetid = models.CharField(max_length=15, blank=True, null=True)
    parentassetname = models.CharField(max_length=250, blank=True, null=True)
    pwbreferencename = models.CharField(max_length=500, blank=True, null=True)
    cased = models.CharField(max_length=50, blank=True, null=True)
    criticalcrossingtype = models.CharField(max_length=50, blank=True, null=True)
    roadcrossing = models.CharField(max_length=50, blank=True, null=True)
    railcrossing = models.CharField(max_length=250, blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pressurized_mains'


class RegionalDrinkingWaterAdvisoryBoundary(models.Model):
    objectid = models.AutoField(primary_key=True)
    phoneno = models.CharField(max_length=20, blank=True, null=True)
    display = models.SmallIntegerField(blank=True, null=True)
    analysis = models.SmallIntegerField(blank=True, null=True)
    bullrunyn = models.SmallIntegerField(blank=True, null=True)
    color = models.SmallIntegerField(blank=True, null=True)
    source = models.CharField(max_length=30, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'regional_drinking_water_advisory_boundary'


class RegionalWaterDistricts(models.Model):
    objectid_1 = models.AutoField(primary_key=True)
    objectid = models.FloatField(blank=True, null=True)
    phoneno = models.CharField(max_length=20, blank=True, null=True)
    display = models.SmallIntegerField(blank=True, null=True)
    analysis = models.SmallIntegerField(blank=True, null=True)
    bullrunyn = models.SmallIntegerField(blank=True, null=True)
    color = models.SmallIntegerField(blank=True, null=True)
    source = models.CharField(max_length=30, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'regional_water_districts'


class Services(models.Model):
    objectid = models.AutoField(primary_key=True)
    accountid = models.FloatField(blank=True, null=True)
    addressnumber = models.CharField(max_length=12, blank=True, null=True)
    alternatenumber = models.CharField(max_length=12, blank=True, null=True)
    streetprefix = models.CharField(max_length=12, blank=True, null=True)
    street = models.CharField(max_length=60, blank=True, null=True)
    streettype = models.CharField(max_length=6, blank=True, null=True)
    multiple = models.CharField(max_length=72, blank=True, null=True)
    addition = models.CharField(max_length=100, blank=True, null=True)
    lot = models.CharField(max_length=30, blank=True, null=True)
    block = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    propertyid = models.FloatField(blank=True, null=True)
    criticalcustomer = models.CharField(max_length=5, blank=True, null=True)
    permitnumber = models.CharField(max_length=15, blank=True, null=True)
    servicesize = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=6, blank=True, null=True)
    depthinches = models.IntegerField(blank=True, null=True)
    pavementmaterial = models.CharField(max_length=20, blank=True, null=True)
    ccloc1 = models.CharField(max_length=50, blank=True, null=True)
    ccloc2 = models.CharField(max_length=50, blank=True, null=True)
    curbstopsize = models.FloatField(blank=True, null=True)
    taploc1 = models.CharField(max_length=50, blank=True, null=True)
    taploc2 = models.CharField(max_length=50, blank=True, null=True)
    tapsize = models.FloatField(blank=True, null=True)
    mainsize = models.FloatField(blank=True, null=True)
    mainmaterial = models.CharField(max_length=6, blank=True, null=True)
    quartersection = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    subtype = models.IntegerField(blank=True, null=True)
    facilityid = models.FloatField(blank=True, null=True)
    metersize = models.FloatField(blank=True, null=True)
    metermake = models.CharField(max_length=255, blank=True, null=True)
    meterlocationdetail = models.CharField(max_length=120, blank=True, null=True)
    altlocationdetail = models.CharField(max_length=120, blank=True, null=True)
    serviceindate = models.DateTimeField(blank=True, null=True)
    serviceremvdate = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    tempuid = models.FloatField(blank=True, null=True)
    modifiedby = models.CharField(max_length=20, blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    dimension = models.CharField(max_length=10, blank=True, null=True)
    addnum = models.FloatField(blank=True, null=True)
    servicepointfacilityid = models.FloatField(blank=True, null=True)
    specialconditions = models.CharField(max_length=40, blank=True, null=True)
    flowmeterfacilityid = models.FloatField(blank=True, null=True)
    enabled = models.SmallIntegerField(blank=True, null=True)
    commentary = models.CharField(max_length=250, blank=True, null=True)
    servicebypass = models.CharField(max_length=4, blank=True, null=True)
    synergenid = models.CharField(max_length=17, blank=True, null=True)
    annexationdate = models.DateTimeField(blank=True, null=True)
    annexed = models.CharField(max_length=3, blank=True, null=True)
    researched = models.CharField(max_length=3, blank=True, null=True)
    automatedmeter = models.CharField(max_length=50, blank=True, null=True)
    automatedmetertype = models.CharField(max_length=50, blank=True, null=True)
    installworkorder = models.CharField(max_length=12, blank=True, null=True)
    dataflag = models.CharField(max_length=3, blank=True, null=True)
    av_oid = models.FloatField(blank=True, null=True)
    facility_folder = models.CharField(max_length=500, blank=True, null=True)
    projectnumber = models.CharField(max_length=20, blank=True, null=True)
    removalproject = models.CharField(max_length=20, blank=True, null=True)
    flushingreason = models.CharField(max_length=250, blank=True, null=True)
    flushingcycle = models.CharField(max_length=3, blank=True, null=True)
    location_no = models.FloatField(blank=True, null=True)
    meternumber = models.CharField(max_length=50, blank=True, null=True)
    parentassetid = models.CharField(max_length=15, blank=True, null=True)
    parentassetname = models.CharField(max_length=250, blank=True, null=True)
    pwbreferencename = models.CharField(max_length=500, blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'services'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'
