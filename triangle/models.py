from django.db import models

class Triangle(models.Model):
    first_side = models.DecimalField(max_digits=5, decimal_places=2)
    second_side=models.DecimalField(max_digits=5, decimal_places=2)
    third_side=models.DecimalField(max_digits=5, decimal_places=2)
    area=models.DecimalField(max_digits=15, decimal_places=2)
