# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Camp(models.Model):
    id_camp = models.CharField(unique=True, max_length=7)
    codice_p = models.ForeignKey('Sito', db_column='codice_p')
    data_c = models.DateTimeField(blank=True, null=True)
    data_r = models.DateTimeField(blank=True, null=True)
    monit = models.ForeignKey('Monit', db_column='monit')
    quota_f = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    id_sito = models.IntegerField()
    nr = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'camp'


class Forn(models.Model):
    forn = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'forn'


class FornCamp(models.Model):
    id_camp = models.ForeignKey(Camp, db_column='id_camp')
    forn = models.ForeignKey(Forn, db_column='forn')

    class Meta:
        managed = False
        db_table = 'forn_camp'


class Lim(models.Model):
    id_par = models.ForeignKey('Par', db_column='id_par')
    par = models.TextField()
    acc = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    mdl = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    metodo = models.TextField(blank=True, null=True)
    data = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lim'


class M(models.Model):
    n_val = models.DecimalField(max_digits=11, decimal_places=6, blank=True, null=True)
    id_prof = models.ForeignKey('Prof', db_column='id_prof')
    id_par = models.ForeignKey('Par', db_column='id_par', unique=True)
    t_val = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm'


class Monit(models.Model):
    tipo = models.CharField(unique=True, max_length=4)
    descr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monit'


class Par(models.Model):
    id = models.AutoField(unique=True)
    par = models.TextField()
    unit = models.TextField(blank=True, null=True)
    matr = models.TextField()
    id_monit = models.ForeignKey(Monit, db_column='id_monit')
    analisi = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'par'
        unique_together = (('id', 'par', 'matr'),)


class Prof(models.Model):
    prof = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    id_camp = models.ForeignKey(Camp, db_column='id_camp', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prof'


class Punto(models.Model):
    codice = models.CharField(primary_key=True, max_length=13)
    data_r = models.DateTimeField(blank=True, null=True)
    geom = models.PointField(srid=102092, blank=True, null=True)
    id = models.AutoField()
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'punto'


class Sito(models.Model):
    codice = models.ForeignKey(Punto, db_column='codice', unique=True)
    descr = models.TextField(blank=True, null=True)
    pma = models.IntegerField()
    y = models.DecimalField(max_digits=10, decimal_places=3)
    x = models.DecimalField(max_digits=10, decimal_places=3)
    lat = models.TextField()
    lon = models.TextField()
    quota = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    foto = models.TextField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sito'
