from django.urls import path
from ventas_app import views

urlpatterns = [
    path('ventas',views.inicio_vistaVentas,name="ventas"),
    path("registrarVentas/", views.registrarVentas, name="registrarVentas"),
    path("borrarVentas/<id_venta>",views.borrarVentas, name="borrarVentas"),
    path("seleccionarVentas/<id_venta>", views.seleccionarVentas, name="selecionarVentas"),
    path("editarVentas/", views.editarVentas, name="editarVentas")
]