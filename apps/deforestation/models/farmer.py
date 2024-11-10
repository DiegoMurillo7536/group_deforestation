from django.db import models

class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    document = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    land_type = models.CharField(max_length=50)
    land_extension = models.DecimalField(max_digits=10, decimal_places=2)
    land_affectations = models.TextField(null=True, blank=True)
    sustainable_techniques = models.BooleanField(default=False)
    annual_production = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    crop_type =models.CharField(max_length=100, null=True, blank=True)
    number_of_employees = models.IntegerField(null=True, blank=True)
    create_at =models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)

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