from django.urls import path, include
from actividad.views import BrigadaCreateView

app_name = 'actividad'

urlpatterns = [
    path('actividad', BrigadaCreateView.as_view(), name='form_brig' )
]
