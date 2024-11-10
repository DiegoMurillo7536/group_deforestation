from django.db import models

class LoggingCompanies(models.Model):
    corporation_id = models.AutoField(primary_key=True, verbose_name="ID Corporaciones")
    name_cop = models.CharField(max_length=100, verbose_name="Nombre Corporaciones")
    headquarters_cop = models.CharField(max_length=100, verbose_name="Sede Corporaciones")
    locations_tala = models.CharField(max_length=100, verbose_name="Lugares de tala")
    reforested_areas = models.CharField(max_length=100, verbose_name="Areas reforestadas")
    annual_wood_volume = models.FloatField(null=True, blank=True, verbose_name="Volumen anual de madera")  
    wood_type = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tipo de madera")
    environmental_alliances = models.CharField(max_length=100, null=True, blank=True, verbose_name="Alianzas ambientales")
    annual_income = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Ingresos anuales") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    government = models.ForeignKey(
        'Governments',
        on_delete=models.CASCADE,
        db_column='id_government',
        verbose_name='Gobierno',
        related_name='LoggingCompanies'
    )

    class Meta:
        db_table = 'logging_companies'

    def __str__(self):
        return self.name_cop
    