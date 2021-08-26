from django.db import models
from uuid import uuid4


class Seed(models.Model):
    # Water constants and choices
    WATER_LOW = 0
    WATER_MEDIUM = 1
    WATER_HIGH = 2
    WATER_CHOICES = [
        (WATER_LOW, 'Low need'),
        (WATER_MEDIUM, 'Medium need'),
        (WATER_HIGH, 'High need')
    ]
    # Sun constants and choices
    SUN_LOW = 0
    SUN_MEDIUM = 1
    SUN_HIGH = 2
    SUN_CHOICES = [
        (SUN_LOW, 'Shadow'),
        (SUN_MEDIUM, 'Half shadow'),
        (SUN_HIGH, 'Sun')
    ]

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    name = models.CharField(null=False, blank=False, max_length=100)
    origin = models.CharField(null=True, blank=False, max_length=100)
    sowing_months = models.CharField(null=True, blank=False, max_length=100)
    days_until_harvest = models.IntegerField(null=True, blank=False)
    min_temperature = models.DecimalField(null=True, blank=False, max_digits=4, decimal_places=2)
    max_temperature = models.DecimalField(null=True, blank=False, max_digits=4, decimal_places=2)
    productivity = models.IntegerField(null=True, blank=False)
    transplant = models.BooleanField(null=True, blank=False)
    germination_days = models.IntegerField(null=True, blank=False)
    water_needed = models.IntegerField(choices=WATER_CHOICES, null=True, blank=False)
    sun_requirement = models.IntegerField(choices=SUN_CHOICES)
    auxiliar_seeds = models.ManyToManyField("seed.Seed", verbose_name=("Auxiliar seeds"))
    auxiliar_plants = models.TextField(null=True, blank=False)

    def save(self, *args, **kwargs):
        # create short uuid
        if self.uniqueId is None:
            self.uniqueId =str(uuid4()).split('-')[1]
        
        super(Seed, self).save(*args, **kwargs)
