from django.contrib import admin
from .models.ambientalist_ong import AmbientalistOng
from .models.governments import Governments
from .models.companies import Companies
from .models.real_state_developers import RealEstateDeveloper
from .models.tourist import Tourist
from .models.farmer import Farmer
from .models.logging_companies import LoggingCompanies
from .models.consumers import Consumers
from .models.indigenous_communities import IndigenousCommunities
# Register your models here.
admin.site.register(AmbientalistOng)
admin.site.register(Governments)
admin.site.register(Companies)
admin.site.register(RealEstateDeveloper)
admin.site.register(Tourist)
admin.site.register(Farmer)
admin.site.register(LoggingCompanies)
admin.site.register(Consumers)
admin.site.register(IndigenousCommunities)
