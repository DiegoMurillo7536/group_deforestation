from django.db import models
class Tourist(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="ID Turistas")
    first_name  = models.CharField(max_length=100, verbose_name="Nombres")
    last_name = models.CharField(max_length=100, verbose_name="Apellidos")
    country_of_origin = models.CharField(max_length=100, verbose_name="Ciudad de Nacimiento")
    date_of_birth  = models.DateField(auto_now_add=False, verbose_name="Fecha de Cumpleaños")
    gender = models.CharField(max_length=1,
    choices=[
            ('F', 'Femenino'),
            ('M', 'Masculino'),
            ('O', 'Otro')], verbose_name="Genero")
    tourist_destination= models.CharField(max_length=100, verbose_name="Destino Turistico")
    arrival_date = models.DateTimeField(auto_now_add=False, verbose_name="Fecha de llegada")
    departure_date = models.DateTimeField(auto_now_add=False, verbose_name="Fecha de Salida")

    realestatedeveloper = models.ForeignKey(
        'RealEstateDeveloper',
        on_delete=models.CASCADE,
        db_column='property_id',
        verbose_name='Desarrollador Inmobiliario',
        related_name='tourists'
    )

    class Meta:
        db_table = 'tourists'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"