# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FormsWorkspace'
        db.create_table('zorna_forms_workspace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entity_content_type_forms_formsworkspace_related', null=True, to=orm['contenttypes.ContentType'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='site_owner_forms_formsworkspace_related', null=True, to=orm['sites.Site'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_owner_forms_formsworkspace_related', null=True, to=orm['auth.User'])),
            ('modifier', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_modifier_forms_formsworkspace_related', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150, db_index=True)),
        ))
        db.send_create_signal('forms', ['FormsWorkspace'])

        # Adding model 'FormsList'
        db.create_table('zorna_forms_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('workspace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.FormsWorkspace'])),
        ))
        db.send_create_signal('forms', ['FormsList'])

        # Adding model 'FormsListEntry'
        db.create_table('zorna_forms_list_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.FormsList'])),
        ))
        db.send_create_signal('forms', ['FormsListEntry'])

        # Adding model 'FormsMasterField'
        db.create_table('zorna_forms_master_field', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('field_type', self.gf('django.db.models.fields.IntegerField')()),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.FormsList'], null=True, blank=True)),
            ('workspace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.FormsWorkspace'])),
        ))
        db.send_create_signal('forms', ['FormsMasterField'])

        # Adding model 'FormsForm'
        db.create_table('zorna_forms_form', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entity_content_type_forms_formsform_related', null=True, to=orm['contenttypes.ContentType'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='site_owner_forms_formsform_related', null=True, to=orm['sites.Site'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_owner_forms_formsform_related', null=True, to=orm['auth.User'])),
            ('modifier', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_modifier_forms_formsform_related', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('button_text', self.gf('django.db.models.fields.CharField')(default=u'Submit', max_length=50)),
            ('bind_to_account', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('response', self.gf('django.db.models.fields.TextField')()),
            ('send_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_from', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('email_copies', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('email_subject', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('email_message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('template', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('workspace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.FormsWorkspace'])),
        ))
        db.send_create_signal('forms', ['FormsForm'])

        # Adding model 'FormsFormField'
        db.create_table('zorna_forms_form_field', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fields', to=orm['forms.FormsForm'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, db_index=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('default_value', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default_master_value', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.FormsListEntry'], null=True, blank=True)),
            ('field_master', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.FormsMasterField'])),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('forms', ['FormsFormField'])

        # Adding model 'FormsFormEntry'
        db.create_table('zorna_forms_form_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entity_content_type_forms_formsformentry_related', null=True, to=orm['contenttypes.ContentType'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='site_owner_forms_formsformentry_related', null=True, to=orm['sites.Site'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_owner_forms_formsformentry_related', null=True, to=orm['auth.User'])),
            ('modifier', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_modifier_forms_formsformentry_related', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['forms.FormsForm'])),
        ))
        db.send_create_signal('forms', ['FormsFormEntry'])

        # Adding model 'FormsFieldEntry'
        db.create_table('zorna_forms_field_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.FormsFormField'])),
            ('form_entry', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fields', to=orm['forms.FormsFormEntry'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('forms', ['FormsFieldEntry'])


    def backwards(self, orm):
        
        # Deleting model 'FormsWorkspace'
        db.delete_table('zorna_forms_workspace')

        # Deleting model 'FormsList'
        db.delete_table('zorna_forms_list')

        # Deleting model 'FormsListEntry'
        db.delete_table('zorna_forms_list_entry')

        # Deleting model 'FormsMasterField'
        db.delete_table('zorna_forms_master_field')

        # Deleting model 'FormsForm'
        db.delete_table('zorna_forms_form')

        # Deleting model 'FormsFormField'
        db.delete_table('zorna_forms_form_field')

        # Deleting model 'FormsFormEntry'
        db.delete_table('zorna_forms_form_entry')

        # Deleting model 'FormsFieldEntry'
        db.delete_table('zorna_forms_field_entry')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'forms.formsfieldentry': {
            'Meta': {'object_name': 'FormsFieldEntry', 'db_table': "'zorna_forms_field_entry'"},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.FormsFormField']"}),
            'form_entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['forms.FormsFormEntry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        'forms.formsform': {
            'Meta': {'object_name': 'FormsForm', 'db_table': "'zorna_forms_form'"},
            'bind_to_account': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'button_text': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_content_type_forms_formsform_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_copies': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email_from': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_subject': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_modifier_forms_formsform_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_owner_forms_formsform_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'response': ('django.db.models.fields.TextField', [], {}),
            'send_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'site_owner_forms_formsform_related'", 'null': 'True', 'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'template': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'workspace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.FormsWorkspace']"})
        },
        'forms.formsformentry': {
            'Meta': {'object_name': 'FormsFormEntry', 'db_table': "'zorna_forms_form_entry'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_content_type_forms_formsformentry_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['forms.FormsForm']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_modifier_forms_formsformentry_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_owner_forms_formsformentry_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'site_owner_forms_formsformentry_related'", 'null': 'True', 'to': "orm['sites.Site']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'forms.formsformfield': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'FormsFormField', 'db_table': "'zorna_forms_form_field'"},
            'default_master_value': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.FormsListEntry']", 'null': 'True', 'blank': 'True'}),
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'field_master': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.FormsMasterField']"}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['forms.FormsForm']"}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'forms.formslist': {
            'Meta': {'object_name': 'FormsList', 'db_table': "'zorna_forms_list'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'workspace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.FormsWorkspace']"})
        },
        'forms.formslistentry': {
            'Meta': {'object_name': 'FormsListEntry', 'db_table': "'zorna_forms_list_entry'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.FormsList']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'forms.formsmasterfield': {
            'Meta': {'object_name': 'FormsMasterField', 'db_table': "'zorna_forms_master_field'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.FormsList']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'workspace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.FormsWorkspace']"})
        },
        'forms.formsworkspace': {
            'Meta': {'ordering': "['name']", 'object_name': 'FormsWorkspace', 'db_table': "'zorna_forms_workspace'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_content_type_forms_formsworkspace_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_modifier_forms_formsworkspace_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_owner_forms_formsworkspace_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'site_owner_forms_formsworkspace_related'", 'null': 'True', 'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'db_index': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['forms']
