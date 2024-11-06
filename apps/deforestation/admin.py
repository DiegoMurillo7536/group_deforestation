from django.contrib import admin
from .models.ambientalist_ong import AmbientalistOng
from .models.governments import Governments

# Register your models here.
admin.site.register(AmbientalistOng)
admin.site.register(Governments)