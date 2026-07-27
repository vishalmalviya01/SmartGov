from django.db import models

class Grievance(models.Model):
    description = models.TextField()
    live_image = models.ImageField(upload_to='complaints/')
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    created_at = models.DateTimeField(auto_now_add=True)