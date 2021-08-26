from django.contrib import admin
from seed.models import Seed

class SeedAdmin(admin.ModelAdmin):
    exclude = ('uniqueId',)
    filter_horizontal = ('auxiliar_seeds',)
admin.site.register(Seed, SeedAdmin)