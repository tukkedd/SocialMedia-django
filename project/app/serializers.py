from rest_framework import serializers
from .models import Usuario, Publicacion, Like, Comentario, Amistad

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'password']

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['id', 'usuario', 'contenido', 'fecha_creacion']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'usuario', 'publicacion', 'fecha_creacion']

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'usuario', 'publicacion', 'contenido', 'fecha_creacion']

class AmistadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amistad
        fields = ['__all__']