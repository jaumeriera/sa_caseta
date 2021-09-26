from django.contrib import admin
from seed.models import Seed, SeedOrigin

class SeedAdmin(admin.ModelAdmin):
    exclude = ('uniqueId',)
    save_as = True
    filter_horizontal = ('auxiliar_seeds', 'sowing_months')
    list_display = ('name', 'uniqueId', 'origin', 'sun_needed',
                    'water_needed', 'get_months')
    fieldsets = (
            ('General info', {
                'fields': ('name', 'scientific_name', 'origin',
                           'water_needed', 'sun_needed', 'min_temperature',
                           'max_temperature', 'productivity')
            }),
            ('Germination', {
                'fields': ('germination_temperature', 'germination_days',
                           'transplant')
            }),
            ('Sowing', {
                'fields': ('sowing_months', 'days_until_harvest')
            }),
            ('Auxiliar', {
                'fields': ('auxiliar_seeds', 'auxiliar_plants')
            }),
            ('Miscelania', {
                'fields': ('comments',)
            })
    )

class SeedOriginAdmin(admin.ModelAdmin):
    pass

admin.site.register(SeedOrigin, SeedOriginAdmin)
admin.site.register(Seed, SeedAdmin)
