# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MaterialItem'
        db.create_table(u'api_materialitem', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parentcollection', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['api.MaterialCollection'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'api', ['MaterialItem'])

        # Adding model 'MaterialCollection'
        db.create_table(u'api_materialcollection', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parentcollection', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['api.MaterialCollection'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'api', ['MaterialCollection'])


    def backwards(self, orm):
        # Deleting model 'MaterialItem'
        db.delete_table(u'api_materialitem')

        # Deleting model 'MaterialCollection'
        db.delete_table(u'api_materialcollection')


    models = {
        u'api.materialcollection': {
            'Meta': {'object_name': 'MaterialCollection'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parentcollection': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['api.MaterialCollection']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'api.materialitem': {
            'Meta': {'object_name': 'MaterialItem'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parentcollection': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['api.MaterialCollection']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['api']