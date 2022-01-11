from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from mastersheet.models import Round2database
# Register your models here.

admin.site.register(Round2database)

# @admin.register(Round2database)
# class Round2databaseAdmin(ImportExportModelAdmin):
#     list_display = ("name", "roll", "number", "email")