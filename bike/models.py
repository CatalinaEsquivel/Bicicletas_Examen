from django.db import models

# Create your models here.
class tipoBicicleta(models.Model):
    idTipoBicicleta = models.IntegerField(primary_key=True,verbose_name='Id tipo bicicleta')
    nombreTipoBicicleta = models.CharField(max_length=20,verbose_name='Nombre tipo de bicicleta')

    def __str__(self):
        return self.nombreTipoBicicleta


class Bicicleta(models.Model):
    idBicicleta = models.CharField(max_length=6,primary_key=True, verbose_name='Código')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    imagen = models.ImageField(upload_to="productos", null=True, blank=True)
    descripcionBicicleta = models.CharField(max_length=300,verbose_name='Descripción')
    precio = models.IntegerField(default=00000000000, verbose_name='Precio')
    tipoBicicleta = models.ForeignKey(tipoBicicleta, on_delete=models.CASCADE)

    def __str__(self):
        return self.idBicicleta
    