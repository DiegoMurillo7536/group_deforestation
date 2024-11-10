from django.db import models

class Consumers(models.Model):
    consumer_id = models.AutoField(primary_key=True)
    consumer_type = models.CharField(max_length=100,choices=[('Individual','individual'), ('Corporativo','corporativo')])
    name = models.CharField(max_length=100)
    purchased_products = models.CharField(max_length=100)
    supports_sustainability = models.BooleanField()
    geographic_location = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    sustainable_certification = models.BooleanField()
    consumption_start_date = models.DateField()
    comments = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
     # Goverment foreign key
    government = models.ForeignKey(
        'Governments',
        on_delete=models.CASCADE,
        db_column='id_government',
        verbose_name='Government',
        related_name='Consumers'
    )

    class Meta:
        db_table = 'consumers'
    
    def __str__(self):
        return self.name
        
