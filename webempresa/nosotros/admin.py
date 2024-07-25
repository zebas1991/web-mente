from django.contrib import admin
from .models import Nosotros

# Register your models here.

class NosotrosAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'puesto', 'trayectoria')
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Nosotros, NosotrosAdmin)