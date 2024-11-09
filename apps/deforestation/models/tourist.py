from django.db import models
class Tourist(models.Model):

    id = models.AutoField(primary_key=True)
    first_name  = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    date_of_birth  = models.DateField(auto_now_add=False)
    gender = models.CharField(max_length=1,
    choices=[
            ('F', 'Femenino'),
            ('M', 'Masculino'),
            ('O', 'Otro')])
    tourist_destination= models.CharField(max_length=100)
    arrival_date = models.DateTimeField(auto_now_add=False)
    departure_date = models.DateTimeField(auto_now_add=False)

    realestatedeveloper = models.ForeignKey(
        'RealEstateDeveloper',
        on_delete=models.CASCADE,
        db_column='property_id',
        verbose_name='Property',
        related_name='tourists'
    )

    class Meta:
        db_table = 'tourists'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"