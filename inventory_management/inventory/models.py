from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ProjectType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ExardProduct(models.Model):
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=255)
    alpha_number = models.CharField(max_length=100)
    bap_number = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

class ProjectAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

class AddUserSubmission(models.Model):
    project_type = models.ForeignKey(ProjectType, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.project_type}"
    

    