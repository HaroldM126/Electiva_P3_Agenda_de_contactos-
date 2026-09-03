from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Contacto
from .forms import ContactoForm

def contacto_lista(request):

    query = request.GET.get('q', '').strip()
    tipo_filtro = request.GET.get('tipo', '').strip()

    contactos = Contacto.objects.all()

    if query:
        contactos = contactos.filter(
            Q(nombre_completo__icontains=query) |
            Q(correo__icontains=query) |
            Q(ciudad__icontains=query) |
            Q(empresa_dependencia__icontains=query)
        )

    if tipo_filtro:
        contactos = contactos.filter(tipo_contacto=tipo_filtro)

    total_contactos = Contacto.objects.count()
    tipos_disponibles = Contacto.TIPO_CHOICES

    context = {
        'contactos': contactos,
        'query': query,
        'tipo_filtro': tipo_filtro,
        'total_contactos': total_contactos,
        'tipos_disponibles': tipos_disponibles,
    }
    return render(request, 'contactos/contacto_lista.html', context)


def contacto_detalle(request, pk):

    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'contactos/contacto_detalle.html', {'contacto': contacto})


def contacto_crear(request):

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nuevo_contacto = form.save()
            messages.success(request, f'¡El contacto "{nuevo_contacto.nombre_completo}" se registró con éxito!')
            return redirect('contacto_lista')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = ContactoForm()

    return render(request, 'contactos/contacto_formulario.html', {
        'form': form,
        'titulo_accion': 'Nuevo Contacto',
        'boton_texto': 'Guardar Contacto'
    })


def contacto_editar(request, pk):

    contacto = get_object_or_404(Contacto, pk=pk)

    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            contacto_actualizado = form.save()
            messages.success(request, f'¡Contacto "{contacto_actualizado.nombre_completo}" actualizado correctamente!')
            return redirect('contacto_detalle', pk=contacto.pk)
        else:
            messages.error(request, 'Ocurrió un error al actualizar los datos.')
    else:
        form = ContactoForm(instance=contacto)

    return render(request, 'contactos/contacto_formulario.html', {
        'form': form,
        'contacto': contacto,
        'titulo_accion': f'Editar Contacto: {contacto.nombre_completo}',
        'boton_texto': 'Actualizar Contacto'
    })


def contacto_eliminar(request, pk):

    contacto = get_object_or_404(Contacto, pk=pk)

    if request.method == 'POST':
        nombre = contacto.nombre_completo
        contacto.delete()
        messages.success(request, f'El contacto "{nombre}" fue eliminado con éxito.')
        return redirect('contacto_lista')

    return render(request, 'contactos/contacto_confirmar_eliminar.html', {'contacto': contacto})
