from django.db import models
# Create your models here.
class AmbientalistOng(models.Model):
    id_ong = models.AutoField(primary_key=True, verbose_name='ID del ONG')
    name = models.CharField(max_length=100, verbose_name=' Nombre del ONG')
    register_number = models.CharField(max_length=100, verbose_name='Registro ONG')
    country = models.CharField(max_length=100, verbose_name='País ONG')
    mission = models.CharField(max_length=100, verbose_name='Misión ONG')
    activities_type = models.CharField(max_length=100, verbose_name='Tipo de actividades ONG')
    focus_area = models.CharField(max_length=100, verbose_name='Área de enfoque ONG')
    annual_budget = models.IntegerField(verbose_name='Presupuesto anual ONG')
    employees_quantity = models.IntegerField(verbose_name='Cantidad de empleados ONG')
    problematic = models.CharField(max_length=100, verbose_name='Problemática ONG')
    current_projects = models.CharField(max_length=100, verbose_name='Proyectos actuales ONG')
    obtained_results = models.CharField(max_length=100, verbose_name='Resultados obtenidos ONG')
    foundation_date = models.DateField(verbose_name='Fecha fundación ONG')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación ONG')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha actualización ONG')

    class Meta:
        db_table = 'ambientalist_ong'
    
    def __str__(self):
        return self.name