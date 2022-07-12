from django.conf import settings
from .views import home
from django.conf.urls.static import static
from xml.dom.minidom import Document
from django.urls import path
from .views import index, iniciosesion, registro, bicicletas, home, form_bicicleta, form_mod_bicicleta, form_de_bicicleta, register,agregar_producto,eliminar_producto,restar_producto,limpiar_carrito
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', index, name='admin-index'),
    path('bicicletas/', bicicletas, name='bicicletas'),
]

urlpatterns = [
    path('',home,name='home'),
    path('form_bicicleta',form_bicicleta,name="form_bicicleta"),
    path('modificar-bicicleta/<id>', form_mod_bicicleta, name="form_mod_bicicleta"),
    path('eliminar-bicicleta/<id>', form_de_bicicleta, name="form_de_bicicleta"),
    path('registro/', registro, name="registro"),
    path('iniciosesion/', iniciosesion, name='iniciosesion'),
    path('index/', index, name='index'),
    path('bicicletas/', bicicletas, name='bicicletas'),
    path('register/', register, name='register'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]

# if settings.DEBUG:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)