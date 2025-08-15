from django.contrib import admin
from myapp.models import Device

# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'pin')
    # Uncomment the following lines if you want to add filtering and search functionality
    # list_filter = ('enabled',)
    # search_fields = ('name',)

admin.site.register(Device, DeviceAdmin)
