from rest_framework.viewsets import ModelViewSet

from livraria_marcus.models import Categoria
from livraria_marcus.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer