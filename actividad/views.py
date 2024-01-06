from django.shortcuts import render
from django.views.generic import FormView

from actividad.forms import BrigadaForm
from actividad.models import Brigada

# Create your views here.
class BrigadaFormView(FormView):
    model = Brigada
    template_name = 'form_brig.html'
    form_class = BrigadaForm
