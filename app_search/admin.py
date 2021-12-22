from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.


@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):
    list_display = ['question', 'answer']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass