from django.db import models
from django.contrib.auth.models import User
from django.db.models import QuerySet


# Create your models here.
class Empresa(models.Model):
    nombre_emp = models.CharField(
        verbose_name='Nombre Empresa', max_length=255,
        unique=True, help_text='Nombre completo de la empresa.'
    )
    documento = models.CharField(
        verbose_name='Numero de Identificación',
        unique=True, max_length=20,
        help_text='Ej: 1234567890123.'
    )
    direccion = models.CharField(
        verbose_name='Dirección', max_length=100,
        help_text='Ej: Calle 100 # 40 - 60'
    )

    def __str__(self):
        return f'{self.nombre_emp.title()}'


class Sede(models.Model):
    nombre_sede = models.CharField(
        verbose_name='Nombre de Sede',
        max_length=50,
    )

    def __str__(self):
        text = f'{self.nombre_sede.title()}'
        return text


class Servicio(models.Model):
    nombre_serv = models.CharField(
        verbose_name='Nombre de los servicios', max_length=100,
        help_text='Nombre del servicio'
    )

    def __str__(self) -> str:
        return f'{self.nombre_serv.title()}'


class Brigada(models.Model):
    nombre_brig = models.CharField(
        verbose_name='Nombre Brigada', max_length=255,
        help_text='Nombre completo de la brigada.'
    )
    f_inicio = models.DateField(
        verbose_name='fecha de Programación',
        blank=False, null=False,
        help_text='Programación de asistencia de la brigada.'
    )
    f_final = models.DateField(
        verbose_name='fecha de Programación',
        help_text='Programación de asistencia del paciente.'
    )
    user = models.ForeignKey(
        User, verbose_name='Usuario',
        on_delete=models.CASCADE
    )
    empresa = models.ForeignKey(
        Empresa, verbose_name='Nombre de empresa',
        on_delete=models.CASCADE
    )

    def save(self):
        if self.f_final == None and self.f_inicio != None:
            self.f_final = self.f_inicio
            return super().save()

    @property
    def examenes(self) -> models.QuerySet['Examen']:
        return self.examen_set.all() # type: ignore

    @property
    def observaciones(self) -> models.QuerySet['Observacion']:
        return self.observacion_set.all() # type: ignore

    @property
    def personas(self) -> list['User']:
        return [
            p.user for p in self.persona_set.all() # type: ignore
        ]

    def __str__(self):
        return f'{self.nombre_brig}'


class Examen(models.Model):
    servicio = models.ForeignKey(
        Servicio, verbose_name='Los servicios que se realizan',
        on_delete=models.CASCADE
    )
    brigada = models.ForeignKey(
        Brigada, verbose_name='Nombre de la briga',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.servicio}'


class Observacion(models.Model):
    text = models.TextField(
        verbose_name='Observaciones adicionales',
        blank=True, null=True,
        help_text='Datos adicionales para tener en cuenta'
    )
    brigada = models.ForeignKey(
        Brigada, verbose_name='Nombre de la briga',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.brigada}'


class Persona(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Personal que va a la brigada',
        on_delete=models.CASCADE
    )
    brigada = models.ForeignKey(
        Brigada, verbose_name='Nombre de la briga',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.user}'