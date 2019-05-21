from django.contrib import admin
from tms.models import Project, Company, Customer, Carrier, Gear, Contract, Line, ContractData

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    pass

@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    pass

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass

@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    pass

@admin.register(ContractData)
class ContractDataAdmin(admin.ModelAdmin):
    pass