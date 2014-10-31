# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlaModel.fdt'
        db.add_column(u'blaapp_blamodel', 'fdt',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 31, 0, 0)),
                      keep_default=False)

        # Adding field 'BlaModel.ft'
        db.add_column(u'blaapp_blamodel', 'ft',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlaModel.fdt'
        db.delete_column(u'blaapp_blamodel', 'fdt')

        # Deleting field 'BlaModel.ft'
        db.delete_column(u'blaapp_blamodel', 'ft')


    models = {
        u'blaapp.blamodel': {
            'Meta': {'object_name': 'BlaModel'},
            'fdt': ('django.db.models.fields.DateTimeField', [], {}),
            'ft': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['blaapp']