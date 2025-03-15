from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE )
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # imagen = models.ImageField(upload_to='publicaciones', storage=fs, blank=True, null=True)   tomandose en cuenta

    def __str__(self):
        return self.contenido

class Like(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'Like de {self.usuario.nombre} en {self.publicacion.contenido}'

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario.nombre} en {self.publicacion.contenido}'

class Amistad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario')
    amigo = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='amigo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Amistad entre {self.usuario.nombre} y {self.amigo.nombre}'

