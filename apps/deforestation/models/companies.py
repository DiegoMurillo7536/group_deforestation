from django.db import models

class Companies(models.Model):
    id_company = models.AutoField(primary_key=True, verbose_name="ID de la empresa")
    name = models.CharField(max_length=100, verbose_name="Nombre de la empresa")
    company_type = models.CharField(max_length=100, verbose_name="Tipo de la empresa")
    location = models.CharField(max_length=100, verbose_name="Ubicación de la empresa")
    foundation_date = models.DateField(verbose_name="Fecha de fundación de la empresa")
    employees_quantity = models.IntegerField(verbose_name="Cantidad de empleados de la empresa")
    mineral_type = models.CharField(max_length=100, verbose_name="Tipo de mineral de la empresa")
    cattle_type = models.CharField(max_length=100, verbose_name="Tipo de ganado de la empresa")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación de la empresa")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización de la empresa")
    
    # Goverment foreign key
    government = models.ForeignKey(
        'Governments',
        on_delete=models.CASCADE,
        db_column='id_government',
        verbose_name='Government',
        related_name='companies'
    )

    class Meta:
        db_table = 'companies'
    
    def __str__(self):
        return self.name