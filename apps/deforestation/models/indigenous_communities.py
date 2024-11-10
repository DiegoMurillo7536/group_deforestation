from django.db import models

class IndigenousCommunities(models.Model):
    community_id = models.AutoField(primary_key=True, verbose_name="Codigo Comunidad")
    community_name = models.CharField(max_length=100, verbose_name="Nombre Comunidad")
    population = models.IntegerField(verbose_name="Poblacion")
    region = models.CharField(max_length=100, verbose_name="Region")
    activities_preservation = models.CharField(max_length=100, verbose_name="Actividades de preservacion")
    deforestation_impact = models.CharField(max_length=100,choices=[('Low','low'), ('Medium','medium'), ('High','high')], verbose_name="Impacto de la deforestación")
    territorial_rights = models.BooleanField(verbose_name="Derechos territoriales")
    support_ong = models.BooleanField(verbose_name="Apoyo ONG")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Goverment foreign key
    government = models.ForeignKey(
        'Governments',
        on_delete=models.CASCADE,
        db_column='id_government',
        verbose_name='Gobiernos',
        related_name='IndigenousCommunities'
    )

    class Meta:
        db_table = 'IndigenousCommunities'
    
    def __str__(self):
        return self.community_name