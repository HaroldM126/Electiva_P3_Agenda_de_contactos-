from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'nombre_completo',
            'correo',
            'telefono',
            'ciudad',
            'empresa_dependencia',
            'tipo_contacto'
        ]
        widgets = {
            'nombre_completo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Ana María Torres',
                'required': 'required'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com',
                'required': 'required'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. +57 312 456 7890',
                'required': 'required'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Mocoa, Pasto, Bogotá',
                'required': 'required'
            }),
            'empresa_dependencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. ITP - Depto. Sistemas / Alcaldía',
                'required': 'required'
            }),
            'tipo_contacto': forms.Select(attrs={
                'class': 'form-select',
                'required': 'required'
            }),
        }
