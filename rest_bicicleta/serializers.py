from rest_framework import serializers
from bike.models import Bicicleta

class BicicletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicicleta
        fields = ['idBicicleta', 'marca', 'imagen', 'descripcionBicicleta', 'precio', 'tipoBicicleta']