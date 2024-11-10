from django.db import models
class RealEstateDeveloper(models.Model):
    property_id = models.AutoField(primary_key=True, verbose_name="Id Desarrollador Inmobiliario")
    name_inm = models.CharField(max_length=100, verbose_name="Nombre inmobiliaria")
    location_inm = models.CharField(max_length=100, verbose_name="Ubicación")
    project_type = models.CharField(max_length=100, verbose_name="Tipo de Proyecto")
    can_projects = models.IntegerField(verbose_name="Cantidad de Proyectos")
    ubi_projects = models.CharField(max_length=100, verbose_name="Ubicación Proyectos")
    environmental_impact_projects = models.CharField(max_length=100, verbose_name="Impacto proyecto ambiental")
    protected_tasks_use = models.CharField(max_length=1,
    choices=[('Y', 'Yes'), ('N', 'No')], verbose_name="Uso de areas protegidas")
    environmental_impact_evaluation = models.BooleanField(default=False, verbose_name="Evaluacion impacto ambiental")
    sustainable_tech_usage = models.CharField(max_length=100, verbose_name="Uso tegnologias sostenibles")
    annual_revenues = models.DecimalField(decimal_places=2,max_digits=11, verbose_name="Ingresos anuales")

    government = models.ForeignKey(
        'Governments',
        on_delete=models.CASCADE,
        db_column='id_government',
        verbose_name='Gobierno',
        related_name='realestatedeveloper'
    )

    class Meta:
        db_table = 'realestatedeveloper'

    def __str__(self):
        return self.name_inm