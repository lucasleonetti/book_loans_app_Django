from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
     
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=50)

    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Libro(models.Model):
        
        titulo = models.CharField(max_length=50)
        autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
        fecha_publicacion = models.DateField()
        genero = models.CharField(max_length=50)
        editorial = models.CharField(max_length=50)
        idioma = models.CharField(max_length=50)
        cantidad_paginas = models.IntegerField()
        imagen = models.ImageField(upload_to='libros/', null=True, blank=True)
        
        def __str__(self):
            return self.titulo

class Prestamo(models.Model):
        
        libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
        fecha_prestamo = models.DateField()
        fecha_devolucion = models.DateField()
        nombre_persona = models.CharField(max_length=50)
        apellido_persona = models.CharField(max_length=50)
        dni = models.IntegerField()
        email = models.EmailField()
        
        def __str__(self):
            return f'{self.nombre_persona} {self.apellido_persona}'
        

class Cliente(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Usuario(models.Model):
        
        nombre_usuario = models.CharField(max_length=50)
        password = models.CharField(max_length=50)
        nombre = models.CharField(max_length=50)
        apellido = models.CharField(max_length=50)
        email = models.EmailField()
        avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
        
        def __str__(self):
            return f'{self.nombre} {self.apellido}'
        
class Avatar(models.Model):
     
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/default.jpg')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # type: ignore
    