from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'correo', 'telefono', 'ciudad', 'empresa_dependencia', 'tipo_contacto', 'fecha_creacion')
    search_fields = ('nombre_completo', 'correo', 'ciudad', 'empresa_dependencia')
    list_filter = ('tipo_contacto', 'ciudad')
