from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import (
    Empresa, Sede, Servicio, Brigada, Examen, Observacion, Persona
)

# Register your models here.
@admin.register(Empresa)
class EmpresaAdmin(ModelAdmin):
    list_display = [
        'nombre_emp', 'documento',
        'direccion'
    ]
    ordering = [
        'nombre_emp'
    ]
    search_fields = [
        'nombre_emp', 'documento',
    ]

@admin.register(Sede)
class SedeAdmin(ModelAdmin):
    list_display = [
        'nombre_sede'
    ]
    search_fields = [
        'nombre_sede'
    ]

@admin.register(Servicio)
class ServicioAdmin(ModelAdmin):
    list_display = [
        'nombre_serv'
    ]
    search_fields =[
        'nombre_serv'
    ]

@admin.register(Brigada)
class BrigadaAdmin(ModelAdmin):
    list_display = [
        'nombre_brig',
        'f_inicio',
        'empresa',
        'user'
    ]
    ordering = [
        'f_inicio'
    ]
    search_fields = [
        'nombre_brig', 'empresa'
    ]

@admin.register(Examen)
class ExamenAdmin(ModelAdmin):
    list_display = [
        'servicio'
    ]
    ordering = [
        'servicio'
    ]
    search_fields = [
        'servicio'
    ]

@admin.register(Observacion)
class ObservacionAdmin(ModelAdmin):
    list_display = [
        'text'
    ]

# @admin.register(Persona)
class PersonaAdmin(ModelAdmin):
    list_display = [
        'user'
    ]
    search_fields = [
        'user'
    ]