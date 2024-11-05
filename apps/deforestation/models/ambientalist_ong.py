from django.db import models
# This is a test
# Create your models here.
class AmbientalistOng(models.Model):
    id_ong = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    mission = models.CharField(max_length=100)
    activities_type = models.CharField(max_length=100)
    focus_area = models.CharField(max_length=100)
    annual_budget = models.IntegerField()
    employees_quantity = models.IntegerField()
    problematic = models.CharField(max_length=100)
    current_projects = models.CharField(max_length=100)
    obtained_results = models.CharField(max_length=100)
    foundation_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'ambientalist_ong'
    
    def __str__(self):
        return self.name