# aqui guardamos las propias urls de cada aplicacion
 
from django.urls import path

# ponemos . porque las views se encuentran en la misma carpeta
from . import views

urlpatterns = [
     # ''= cuando se encuentre en la ruta principal osea = 127.0.0.1:(servidor) 
    path('',views.autor),
    path('ejercicio1/',views.ejercicio1),
    path('ejercicio2/',views.ejercicio2),
    path('ejercicio3/',views.ejercicio3),
    path('ejercicio4/',views.ejercicio4),
    path('ejercicio5/',views.ejercicio5),
    path('ejercicio6/',views.ejercicio6),
    path('ejercicio7/',views.ejercicio7),
    path('ejercicio8/',views.ejercicio8),
    path('ejercicio9/',views.ejercicio9),
    path('ejercicio10/',views.ejercicio10),
    path('ejercicio11/',views.ejercicio11),
    path('ejercicio12/',views.ejercicio12),
    path('ejercicio13/',views.ejercicio13),
    path('ejercicio14/',views.ejercicio14),
    path('ejercicio15/',views.ejercicio15),
    path('mi-url/', views.vista_compuesta,name='mi-url'),
]
