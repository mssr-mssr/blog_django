from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'titulo', 'contenido', 'autor', 'fecha_publicacion']
