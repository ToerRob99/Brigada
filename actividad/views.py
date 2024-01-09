from django.shortcuts import render
from django.views.generic import CreateView

from actividad.forms import BrigadaForm
from actividad.models import Brigada

# Create your views here.
class BrigadaCreateView(CreateView):
    model = Brigada
    context_object_name = 'props'
    template_name = 'form_brig.html'
    form_class = BrigadaForm
