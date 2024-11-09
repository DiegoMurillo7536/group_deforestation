from django.db import models
class RealEstateDeveloper(models.Model):
    property_id = models.AutoField(primary_key=True)
    name_inm = models.CharField(max_length=100)
    location_inm = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    can_projects = models.IntegerField()
    ubi_projects = models.CharField(max_length=100)
    environmental_impact_projects = models.CharField(max_length=100)
    protected_tasks_use = models.CharField(max_length=1,
    choices=[('Y', 'Yes'), ('N', 'No')])
    environmental_impact_evaluation = models.BooleanField(default=False)
    sustainable_tech_usage = models.CharField(max_length=100)
    annual_revenues = models.DecimalField(decimal_places=2,max_digits=11)

    government = models.ForeignKey(
        'Governments',
        on_delete=models.CASCADE,
        db_column='id_government',
        verbose_name='Government',
        related_name='realestatedeveloper'
    )

    class Meta:
        db_table = 'realestatedeveloper'

    def __str__(self):
        return self.name_inm