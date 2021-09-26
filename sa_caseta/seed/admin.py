from django.contrib import admin
from seed.models import Seed

class SeedAdmin(admin.ModelAdmin):
    exclude = ('uniqueId',)
    filter_horizontal = ('auxiliar_seeds', 'sowing_months')
    list_display = ('name', 'uniqueId', 'origin', 'germination_days', 
                    'days_until_harvest', 'sun_needed', 'water_needed')
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

admin.site.register(Seed, SeedAdmin)
