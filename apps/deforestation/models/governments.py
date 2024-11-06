from django.db import models

class Governments(models.Model):
    id_government = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100)
    forest_policy = models.CharField(max_length=100)
    funds_allocated= models.IntegerField()
    commitment_level = models.IntegerField()
    implementation_date = models.DateField()
    protected_areas = models.CharField(max_length=100)
    deforestation_sanctions = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'governments'
    
    def __str__(self):
        return self.country_name