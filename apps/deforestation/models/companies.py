from django.db import models

class Companies(models.Model):
    id_company = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    foundation_date = models.DateField()
    employees_quantity = models.IntegerField()
    mineral_type = models.CharField(max_length=100)
    cattle_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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