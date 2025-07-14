from django.db import models

# Create your models here.
from django.db import models

class ExardProduct(models.Model):
    # product_name = models.CharField(max_length=255)
    alpha_number = models.CharField(max_length=100)
    bap_number = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_name