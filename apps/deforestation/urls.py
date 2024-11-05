from django.urls import path
from .views import ong

urlpatterns = [
    path('', ong.home, ),
    path('add_ong/', ong.add_ong, ),
    path('delete_ong/<int:id_ong>/', ong.delete_ong, ),
    path('edit_ong/<int:id_ong>/', ong.edit_ong,),
    path('update_ong/<int:id_ong>/', ong.update_ong, )
]