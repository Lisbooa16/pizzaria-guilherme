from rest_framework import generics
from restaurante.models import prato
from restaurante.serializers import PratoSerializer


class PratoListView(generics.ListAPIView):
    queryset = prato.objects.all()
    serializer_class =  PratoSerializer