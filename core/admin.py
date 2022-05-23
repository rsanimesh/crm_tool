from django.contrib import admin
from .models import *

admin.site.register(Company)

@admin.register(ApiEndPoint)
class ApiEndPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(MasterData)
class MasterDataAdmin(admin.ModelAdmin):
    list_display = ("id","field_name", 'value', 'validate_value','row_index')

admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Table)
admin.site.register(FieldList)


