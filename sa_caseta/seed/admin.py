from django.contrib import admin
from seed.models import Seed

class SeedAdmin(admin.ModelAdmin):
    exclude = ('uniqueId',)
    filter_horizontal = ('auxiliar_seeds',)
    list_display = ('name', 'uniqueId', 'origin', 'germination_days', 
                    'days_until_harvest', 'sun_needed', 'water_needed')
admin.site.register(Seed, SeedAdmin)