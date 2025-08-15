from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    enabled = models.BooleanField(default=False)
    pin = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} (Enabled: {self.enabled}, Pin: {self.pin})"

    # class Meta:
    #     verbose_name_plural = "Devices"
    #     ordering = ['name']
