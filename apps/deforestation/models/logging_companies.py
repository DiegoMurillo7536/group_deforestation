from django.db import models

class LoggingCompanies(models.Model):
    corporation_id = models.AutoField(primary_key=True)
    name_cop = models.CharField(max_length=100)
    headquarters_cop = models.CharField(max_length=100)
    locations_tala = models.CharField(max_length=100)
    reforested_areas = models.CharField(max_length=100)
    annual_wood_volume = models.FloatField(null=True, blank=True)  
    wood_type = models.CharField(max_length=100, null=True, blank=True)
    environmental_alliances = models.CharField(max_length=100, null=True, blank=True)
    annual_income = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    government = models.ForeignKey(
        'Governments',
        on_delete=models.CASCADE,
        db_column='id_government',
        verbose_name='Government',
        related_name='LoggingCompanies'
    )

    class Meta:
        db_table = 'logging_companies'

    def __str__(self):
        return self.name_cop
    