from rest_framework.serializers import ModelSerializer

from livraria_marcus.models import Categoria, Editora, Autor 

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"