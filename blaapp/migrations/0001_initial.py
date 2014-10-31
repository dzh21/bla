# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlaModel'
        db.create_table(u'blaapp_blamodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'blaapp', ['BlaModel'])


    def backwards(self, orm):
        # Deleting model 'BlaModel'
        db.delete_table(u'blaapp_blamodel')


    models = {
        u'blaapp.blamodel': {
            'Meta': {'object_name': 'BlaModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['blaapp']