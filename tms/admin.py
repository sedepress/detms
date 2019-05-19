from django.contrib import admin
from tms.models import Project, Company

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'parent_id', 'level')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)