from django.db import models

class IndigenousCommunities(models.Model):
    community_id = models.AutoField(primary_key=True)
    community_name = models.CharField(max_length=100)
    population = models.IntegerField()
    region = models.CharField(max_length=100)
    activities_preservation = models.CharField(max_length=100)
    deforestation_impact = models.CharField(max_length=100,choices=[('Low','low'), ('Medium','medium'), ('High','high')])
    territorial_rights = models.BooleanField()
    support_ong = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Goverment foreign key
    government = models.ForeignKey(
        'Governments',
        on_delete=models.CASCADE,
        db_column='id_government',
        verbose_name='Government',
        related_name='IndigenousCommunities'
    )

    class Meta:
        db_table = 'IndigenousCommunities'
    
    def __str__(self):
        return self.community_name