from django.contrib import admin
from .models.ambientalist_ong import AmbientalistOng
from .models.governments import Governments
from .models.companies import Companies
from .models.real_state_developers import RealEstateDeveloper
from .models.tourist import Tourist
# Register your models here.
admin.site.register(AmbientalistOng)
admin.site.register(Governments)
admin.site.register(Companies)
admin.site.register(RealEstateDeveloper)
admin.site.register(Tourist)