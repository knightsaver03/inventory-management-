from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ProjectType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ExardProduct(models.Model):
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, related_name='products')
    alpha_number = models.CharField(max_length=100)
    # bap_number = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.alpha_number
    
class ExcelData(models.Model):
    project_type = models.CharField(max_length=100)
    alpha_number = models.CharField(max_length=100)
    bap_number = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.project_type} - {self.alpha_number} - {self.quantity}"

class AddUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username






    
    