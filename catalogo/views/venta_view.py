from ..models_raiz import Venta
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class VentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venta
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    