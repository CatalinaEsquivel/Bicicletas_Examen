from django.urls import path
from rest_bicicleta.views import lista_bicicletas, detalle_bicicleta
from rest_bicicleta.viewsLogin import login

urlpatterns = [
    path('lista_bicicletas',lista_bicicletas,name="lista_bicicletas"),
    path('detalle_bicicleta/<id>',detalle_bicicleta,name="detalle_bicicleta"),
    path('login',login,name='login'),
]