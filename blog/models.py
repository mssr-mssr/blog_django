from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)  # Corregido max_length
    contenido = models.TextField()  # Corregido TextField y nombre del campo
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
class Comentario (models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"(Comentario de {self.autor} en {self.post.titulo})"

# Topos de campos asicionales
'''
CharField = Texto corto con limitante de caracteres
TextField = Texto largo
DateTime = Fecha y Hora

BooleanField = Booleanos
IntegerField = Números enteros
EmailField = Email o correo vaido

ForeingKey = Relacion muchos a uno
ManyToManyField = Relacion muchos a muchos
'''
# Paso obligatorio despues de manipuar los modelos es hacer MIGRACIONES

'''
python manage.py makemigrations = crea las migraciones 

python manage.py migrate = aplicar los cambios a la base de datos 
'''