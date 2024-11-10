from django.db import models

class Consumers(models.Model):
    consumer_id = models.AutoField(primary_key=True, verbose_name="ID del consumidor")
    consumer_type = models.CharField(max_length=100,choices=[('Individual','individual'), ('Corporativo','corporativo')], verbose_name="Tipo de consumidor")
    name = models.CharField(max_length=100, verbose_name="Nombre del consumidor")
    purchased_products = models.CharField(max_length=100, verbose_name="Productos comprados por el consumidor")
    supports_sustainability = models.BooleanField(verbose_name="¿Soporta la sostenibilidad?")
    geographic_location = models.CharField(max_length=100, verbose_name="Ubicación geográfica del consumidor")
    product_type = models.CharField(max_length=100, verbose_name="Tipo de producto")
    sustainable_certification = models.BooleanField(verbose_name="¿Certificado de sostenibilidad?")
    consumption_start_date = models.DateField(verbose_name="Fecha de inicio de la consumo")
    comments = models.CharField(max_length=100, verbose_name="Comentarios")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del consumidor")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización del consumidor")
    
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
        
