from django.contrib import admin
from .models import Usuario, Publicacion, Like, Comentario, Amistad


# class UsuarioAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'email')

# class PublicacionAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'contenido', 'fecha_creacion')

# class LikeAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'publicacion', 'fecha_creacion')

# class ComentarioAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'publicacion', 'contenido', 'fecha_creacion')

# class AmistadAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'amigo', 'fecha_creacion')




admin.site.register(Usuario)
admin.site.register(Publicacion)
admin.site.register(Like)
admin.site.register(Comentario)
admin.site.register(Amistad)
