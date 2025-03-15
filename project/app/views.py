from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Publicacion, Like, Comentario, Amistad
from .serializers import UsuarioSerializer, PublicacionSerializer, LikeSerializer, ComentarioSerializer, AmistadSerializer

from rest_framework.permissions import IsAuthenticated


    # import pudb; pu.db 


class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Autenticación básica

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer



class PublicacionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class AmistadViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Amistad.objects.all()
    serializer_class = AmistadSerializer
