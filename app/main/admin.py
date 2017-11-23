#coding: utf-8

import os
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from main.forms import FilesAdminForm, WordsAdminForm
from main.models import Words, Files
from main.utils import remove_csv_files



def delete_selected(modeladmin, request, queryset):
	if not modeladmin.has_delete_permission(request, obj=queryset):
		raise PermissionDenied
	for obj in queryset:
		remove_csv_files(str(obj.file))
		obj.delete()

delete_selected.short_description = "Delete selected objects"



class FilesAdmin(admin.ModelAdmin):
	form = FilesAdminForm
	actions = [delete_selected]



class WordsAdmin(admin.ModelAdmin):
	form = WordsAdminForm



admin.site.register(Words, WordsAdmin)
admin.site.register(Files, FilesAdmin)
