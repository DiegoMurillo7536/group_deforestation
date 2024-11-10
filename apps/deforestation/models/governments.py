from django.db import models

class Governments(models.Model):
    id_government = models.AutoField(primary_key=True, verbose_name='ID del gobierno')
    country_name = models.CharField(max_length=100, verbose_name='Nombre del país')
    forest_policy = models.CharField(max_length=100, verbose_name='Política forestal')
    funds_allocated= models.IntegerField(verbose_name='Fondos asignados')
    commitment_level = models.IntegerField(verbose_name='Nivel de compromiso')
    implementation_date = models.DateField(verbose_name='Fecha de implementación')
    protected_areas = models.CharField(max_length=100, verbose_name='Áreas protegidas')
    deforestation_sanctions = models.CharField(max_length=100, verbose_name='Sanciones de deforestación')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del gobierno')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización del gobierno')

    class Meta:
        db_table = 'governments'
    
    def __str__(self):
        return self.country_name