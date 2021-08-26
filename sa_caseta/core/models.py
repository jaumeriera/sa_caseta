from django.db import models

# Create your models here.
class Month(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.name