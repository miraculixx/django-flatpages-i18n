# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FlatPage_i18n.url_sk'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'url_sk')

        # Deleting field 'FlatPage_i18n.url_hu'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'url_hu')

        # Deleting field 'FlatPage_i18n.title_sk'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'title_sk')

        # Deleting field 'FlatPage_i18n.content_hu'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'content_hu')

        # Deleting field 'FlatPage_i18n.title_hu'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'title_hu')

        # Deleting field 'FlatPage_i18n.url_cs'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'url_cs')

        # Deleting field 'FlatPage_i18n.content_sk'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'content_sk')

        # Deleting field 'FlatPage_i18n.content_cs'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'content_cs')

        # Deleting field 'FlatPage_i18n.title_cs'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'title_cs')

        # Adding field 'FlatPage_i18n.url_de'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'url_de',
                      self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.url_en'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'url_en',
                      self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.title_de'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'title_de',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.title_en'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.content_de'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'content_de',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.content_en'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'content_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'MenuItem.title_hu'
        db.delete_column(u'flatpages_i18n_menuitem', 'title_hu')

        # Deleting field 'MenuItem.title_cs'
        db.delete_column(u'flatpages_i18n_menuitem', 'title_cs')

        # Deleting field 'MenuItem.title_sk'
        db.delete_column(u'flatpages_i18n_menuitem', 'title_sk')

        # Adding field 'MenuItem.title_de'
        db.add_column(u'flatpages_i18n_menuitem', 'title_de',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MenuItem.title_en'
        db.add_column(u'flatpages_i18n_menuitem', 'title_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'FlatPage_i18n.url_sk'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'url_sk',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.url_hu'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'url_hu',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.title_sk'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'title_sk',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.content_hu'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'content_hu',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.title_hu'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'title_hu',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.url_cs'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'url_cs',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.content_sk'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'content_sk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.content_cs'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'content_cs',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatPage_i18n.title_cs'
        db.add_column(u'flatpages_i18n_flatpage_i18n', 'title_cs',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'FlatPage_i18n.url_de'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'url_de')

        # Deleting field 'FlatPage_i18n.url_en'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'url_en')

        # Deleting field 'FlatPage_i18n.title_de'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'title_de')

        # Deleting field 'FlatPage_i18n.title_en'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'title_en')

        # Deleting field 'FlatPage_i18n.content_de'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'content_de')

        # Deleting field 'FlatPage_i18n.content_en'
        db.delete_column(u'flatpages_i18n_flatpage_i18n', 'content_en')

        # Adding field 'MenuItem.title_hu'
        db.add_column(u'flatpages_i18n_menuitem', 'title_hu',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MenuItem.title_cs'
        db.add_column(u'flatpages_i18n_menuitem', 'title_cs',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MenuItem.title_sk'
        db.add_column(u'flatpages_i18n_menuitem', 'title_sk',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'MenuItem.title_de'
        db.delete_column(u'flatpages_i18n_menuitem', 'title_de')

        # Deleting field 'MenuItem.title_en'
        db.delete_column(u'flatpages_i18n_menuitem', 'title_en')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'flatpages_i18n.flatpage_i18n': {
            'Meta': {'ordering': "('weight', 'created')", 'object_name': 'FlatPage_i18n'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'machine_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['flatpages_i18n.FlatPage_i18n']"}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['shrfeat.SubSite']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'url_de': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'flatpages_i18n.menuitem': {
            'Meta': {'ordering': "('weight', 'created')", 'object_name': 'MenuItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'custom_link': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'flatpage': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['flatpages_i18n.FlatPage_i18n']", 'null': 'True', 'blank': 'True'}),
            'has_custom_link': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'machine_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['flatpages_i18n.MenuItem']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_de': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'shrfeat.subsite': {
            'Meta': {'object_name': 'SubSite'},
            '_plan': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'features': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'redirect': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['flatpages_i18n']