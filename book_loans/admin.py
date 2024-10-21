from django.contrib import admin
from book_loans.models import Autor, Avatar, Cliente, Libro, Prestamo, Usuario

# Register your models here.

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Avatar)
