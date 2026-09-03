from django.db import models

class Contacto(models.Model):
    TIPO_CHOICES = [
        ('Personal', 'Personal'),
        ('Laboral', 'Laboral'),
        ('Académico', 'Académico'),
        ('Institucional', 'Institucional'),
    ]

    nombre_completo = models.CharField(
        max_length=120,
        verbose_name="Nombre Completo"
    )
    correo = models.EmailField(
        max_length=100,
        verbose_name="Correo Electrónico"
    )
    telefono = models.CharField(
        max_length=20,
        verbose_name="Teléfono / Celular"
    )
    ciudad = models.CharField(
        max_length=80,
        verbose_name="Ciudad"
    )
    empresa_dependencia = models.CharField(
        max_length=100,
        verbose_name="Empresa o Dependencia"
    )
    tipo_contacto = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='Personal',
        verbose_name="Tipo de Contacto"
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Registro"
    )

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['nombre_completo']

    def __str__(self):
        return f"{self.nombre_completo} ({self.tipo_contacto})"
