from django.db import models

# Create your models here.


class InventoryTracker(models.Model):
    name = models.CharField(max_length=180)
    url = models.URLField(blank=True, max_length=1000)
    count = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name
