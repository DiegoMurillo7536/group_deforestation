from django.db import models

class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True, verbose_name='ID del agricultor')
    document = models.CharField(max_length=20,verbose_name='Documento de identidad')
    name = models.CharField(max_length=100, verbose_name='Nombre del agricultor')
    country = models.CharField(max_length=50, verbose_name='País del agricultor')
    land_type = models.CharField(max_length=50, verbose_name='Tipo de tierra del agricultor')
    land_extension = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Extensión de tierra del agricultor')
    land_affectations = models.TextField(null=True, blank=True, verbose_name='Afectaciones del tierra del agricultor')
    sustainable_techniques = models.BooleanField(default=False, verbose_name='Técnicas sostenibles del agricultor')
    annual_production = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='Producción anual del agricultor')
    crop_type =models.CharField(max_length=100, null=True, blank=True, verbose_name='Tipo de cultivo del agricultor')
    number_of_employees = models.IntegerField(null=True, blank=True, verbose_name='Cantidad de empleados del agricultor')
    create_at =models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del agricultor')
    UPDATED_AT = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización del agricultor')

    government = models.ForeignKey(
        'Governments',
        on_delete=models.CASCADE,
        db_column='id_government',
        verbose_name='Government',
        related_name='Farmer'
    )

    ambientalist_ong = models.ForeignKey(
        'AmbientalistOng',
        on_delete=models.CASCADE,
        db_column='id_ong',
        verbose_name='AmbientalistOng',
        related_name='Farmer'
    )

    class Meta:
        db_table ='farmers'

    def __str__(self):
        return self.name