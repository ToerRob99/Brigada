from django.urls import path, include
from actividad.views import BrigadaFormView

app_name = 'actividad'

urlpatterns = [
    path('actividad', BrigadaFormView.as_view(), name='form_brig' )
]
