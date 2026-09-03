from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto_lista, name='contacto_lista'),
    path('crear/', views.contacto_crear, name='contacto_crear'),
    path('<int:pk>/', views.contacto_detalle, name='contacto_detalle'),
    path('<int:pk>/editar/', views.contacto_editar, name='contacto_editar'),
    path('<int:pk>/eliminar/', views.contacto_eliminar, name='contacto_eliminar'),
]
