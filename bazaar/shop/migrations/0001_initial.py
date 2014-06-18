# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MaterialItem'
        db.create_table(u'shop_materialitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mTitle', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=8000)),
            ('owner_org_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('free', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('link', self.gf('django.db.models.fields.TextField')(max_length=8000)),
            ('itemType', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('createdAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date.today)),
            ('lastModified', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('numberOfRatings', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('numberOfLikes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'shop', ['MaterialItem'])

        # Adding model 'Tags'
        db.create_table(u'shop_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('createdAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date.today)),
            ('lastModified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date.today)),
        ))
        db.send_create_signal(u'shop', ['Tags'])

        # Adding model 'ItemTags'
        db.create_table(u'shop_itemtags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('itemId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.MaterialItem'])),
            ('tagsId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Tags'])),
        ))
        db.send_create_signal(u'shop', ['ItemTags'])

        # Adding model 'Ratings'
        db.create_table(u'shop_ratings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rateValue', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('createdAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date.today)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'shop', ['Ratings'])

        # Adding model 'Comment'
        db.create_table(u'shop_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commentText', self.gf('django.db.models.fields.TextField')(max_length=8000)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'shop', ['Comment'])

        # Adding model 'ItemRatings'
        db.create_table(u'shop_itemratings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('itemId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.MaterialItem'])),
            ('ratingsID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Ratings'])),
        ))
        db.send_create_signal(u'shop', ['ItemRatings'])


    def backwards(self, orm):
        # Deleting model 'MaterialItem'
        db.delete_table(u'shop_materialitem')

        # Deleting model 'Tags'
        db.delete_table(u'shop_tags')

        # Deleting model 'ItemTags'
        db.delete_table(u'shop_itemtags')

        # Deleting model 'Ratings'
        db.delete_table(u'shop_ratings')

        # Deleting model 'Comment'
        db.delete_table(u'shop_comment')

        # Deleting model 'ItemRatings'
        db.delete_table(u'shop_itemratings')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'shop.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'commentText': ('django.db.models.fields.TextField', [], {'max_length': '8000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'shop.itemratings': {
            'Meta': {'object_name': 'ItemRatings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemId': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.MaterialItem']"}),
            'ratingsID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Ratings']"})
        },
        u'shop.itemtags': {
            'Meta': {'object_name': 'ItemTags'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemId': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.MaterialItem']"}),
            'tagsId': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Tags']"})
        },
        u'shop.materialitem': {
            'Meta': {'object_name': 'MaterialItem'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'createdAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date.today'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '8000'}),
            'free': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemType': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'lastModified': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'link': ('django.db.models.fields.TextField', [], {'max_length': '8000'}),
            'mTitle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numberOfLikes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'numberOfRatings': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'owner_org_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'shop.ratings': {
            'Meta': {'object_name': 'Ratings'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'createdAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rateValue': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'shop.tags': {
            'Meta': {'object_name': 'Tags'},
            'createdAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastModified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date.today'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['shop']