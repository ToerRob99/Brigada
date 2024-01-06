from django.forms import ModelForm

# import locales del modelo
from actividad.models import (
    Sede, Servicio, Brigada, Examen, Empresa, Observacion, Persona
)

# Modelo del formulario para crear brigada
class BrigadaForm(ModelForm):
    class Meta:
        model = Brigada
        field = [
            'nombre_brig', 'personas'
        ]
        #widgets = {
            #'user': ModelForm.HiddenInput() # type: ignore
        # metodo creador para asignar clase al los elementos del formularios
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
