from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from book_loans.forms import AutorForm, ClienteForm, LibroForm, PrestamosForm, RegistroUsuarioForm, UserEditForm
from book_loans.models import Autor, Avatar, Cliente, Libro, Prestamo

# Create your views here.
def index(req: HttpRequest):
    try:
        avatar = Avatar.objects.get(usuario=req.user.id)
        url_avatar = avatar.imagen.url
    except Avatar.DoesNotExist:
        url_avatar = 'https://www.testhouse.net/wp-content/uploads/2021/11/default-avatar.jpg'  # O puedes proporcionar una URL de avatar predeterminado
    
    return render(req, 'index.html', {'url_avatar': url_avatar})

@login_required
def nuevo_libro(req: HttpRequest):
    
    if req.method == 'POST':
        
        nuevo_libro_form = LibroForm(req.POST)
        
        if nuevo_libro_form.is_valid():
            data = nuevo_libro_form.cleaned_data
            l = Libro(titulo=data['titulo'], autor=data['autor'], fecha_publicacion=data['fecha_publicacion'], genero=data['genero'], editorial=data['editorial'], idioma=data['idioma'], cantidad_paginas=data['cantidad_paginas'])
            l.save()
            return render(req, 'index.html')
        else:
            nuevo_libro_form = LibroForm()
            return render(req, 'abm/create/nuevo_libro.html', {'nuevo_libro_form': nuevo_libro_form})
    else:
        nuevo_libro_form = LibroForm()
        return render(req, 'abm/create/nuevo_libro.html', {'nuevo_libro_form': nuevo_libro_form})

@login_required
def nuevo_prestamo(req: HttpRequest):
    
    if req.method == 'POST':
        
        nuevo_prestamo_form = PrestamosForm(req.POST)
        
        if nuevo_prestamo_form.is_valid():
            data = nuevo_prestamo_form.cleaned_data
            p = Prestamo(libro=data['libro'], fecha_prestamo=data['fecha_prestamo'], fecha_devolucion=data['fecha_devolucion'], nombre_persona=data['nombre_persona'], apellido_persona=data['apellido_persona'], dni=data['dni'], email=data['email'])
            p.save()
            return render(req, 'index.html')
        else:
            nuevo_prestamo_form = PrestamosForm()
            return render(req, 'abm/create/nuevo_prestamo.html', {'nuevo_prestamo_form': nuevo_prestamo_form})
    else:
        nuevo_prestamo_form = PrestamosForm()
        return render(req, 'abm/create/nuevo_prestamo.html', {'nuevo_prestamo_form': nuevo_prestamo_form})

@login_required
def lista_prestamos(req: HttpRequest):
    prestamos = Prestamo.objects.all()
    return render(req, 'abm/read/lista_de_prestamos.html', {'prestamos': prestamos})

def lista_libros(req: HttpRequest):
    libros = Libro.objects.all()
    return render(req, 'abm/read/lista_de_libros.html', {'libros': libros})

@login_required
def lista_clientes(req: HttpRequest):
    
    clientes = Cliente.objects.all()
    return render(req, 'abm/read/lista_clientes.html', {'clientes': clientes})

@login_required
def nuevo_cliente(req: HttpRequest):
    
    if req.method == 'POST':
        
        nuevo_cliente_form = ClienteForm(req.POST)
        
        if nuevo_cliente_form.is_valid():
            data = nuevo_cliente_form.cleaned_data
            c = Cliente(nombre=data['nombre'], apellido=data['apellido'], dni=data['dni'], email=data['email'])
            c.save()
            return render(req, 'index.html')
        else:
            nuevo_cliente_form = ClienteForm()
            return render(req, 'abm/create/nuevo_cliente.html', {'nuevo_cliente_form': nuevo_cliente_form})
    else:
        nuevo_cliente_form = ClienteForm()
        return render(req, 'abm/create/nuevo_cliente.html', {'nuevo_cliente_form': nuevo_cliente_form})
    
def lista_autores(req: HttpRequest):
    autores = Autor.objects.all()
    return render(req, 'abm/read/lista_de_autores.html', {'autores': autores})

@login_required
def nuevo_autor(req: HttpRequest):
        
        if req.method == 'POST':
            
            nuevo_autor_form = AutorForm(req.POST)
            
            if nuevo_autor_form.is_valid():
                data = nuevo_autor_form.cleaned_data
                a = Autor(nombre=data['nombre'], apellido=data['apellido'], fecha_nacimiento=data['fecha_nacimiento'],fecha_defuncion=data['fecha_defuncion'] ,nacionalidad=data['nacionalidad'])
                a.save()
                return render(req, 'index.html')
            else:
                nuevo_autor_form = AutorForm()
                return render(req, 'abm/create/nuevo_autor.html', {'nuevo_autor_form': nuevo_autor_form})
        else:
            nuevo_autor_form = AutorForm()
            return render(req, 'abm/create/nuevo_autor.html', {'nuevo_autor_form': nuevo_autor_form})
        
def user_login(req: HttpRequest):
    
    if req.method == 'POST':
       
        formulario_login = AuthenticationForm(req, data=req.POST)
       
        if formulario_login.is_valid():
            data = formulario_login.cleaned_data
            usuario = data['username']
            password = data['password']
            user = authenticate(req, username=usuario, password=password)
            if user is not None:
                login(req, user)
                return render(req, 'index.html', {"mensaje":f'Bienvenido {usuario}!'})
            else:
                return render(req, 'auth/user_login.html', {'mensaje':'Datos incorrectos, intente nuevamente'})
            
        else:
            return render(req, 'auth/user_login.html', {'mensaje':'Datos incorrectos, intente nuevamente'})
    else:
        formulario_login = AuthenticationForm()
        return render(req, 'auth/user_login.html', {'formulario_login':formulario_login})
    
def registro_usuario(req: HttpRequest):
    
    if req.method == 'POST':
        formulario_login = RegistroUsuarioForm(req.POST)
       
        if formulario_login.is_valid():
            formulario_login.save()
            usuario = formulario_login.cleaned_data.get('username')
            return render(req, 'index.html', {"mensaje":f' El usuario {usuario} ha sido creado exitosamente!'})
        else:
            return render(req, 'auth/registro.html', {'formulario_login':formulario_login, 'mensaje':'Datos incorrectos, intente nuevamente'})
    else:
        formulario_login = RegistroUsuarioForm()
        return render(req, 'auth/registro.html', {'formulario_login':formulario_login})
    
@login_required
def delete_book(req: HttpRequest, id: int):
    
    if req.method == 'POST':
        libro = Libro.objects.get(id=id)
        libro.delete()
        return render(req, 'index.html', {'mensaje':'Libro eliminado exitosamente!'})
    else:
        return render(req, 'index.html', {'mensaje':'Error al eliminar libro!'})

@login_required
def update_book( req: HttpRequest, id: int):
    
    libro = Libro.objects.get(id=id)
    
    if req.method == 'POST':
        
        nuevo_libro_form = LibroForm(req.POST, instance=libro)
        
        if nuevo_libro_form.is_valid():
            nuevo_libro_form.save()
            return render(req, 'index.html', {'mensaje':'Libro actualizado exitosamente!'})
        else:
            nuevo_libro_form = LibroForm(instance=libro)
            return render(req, 'abm/update/update_libro.html', {'nuevo_libro_form': nuevo_libro_form})
    else:
        nuevo_libro_form = LibroForm(instance=libro)
        return render(req, 'abm/update/update_libro.html', {'nuevo_libro_form': nuevo_libro_form})
    
@login_required
def update_user(req: HttpRequest):
    
    usuario = req.user
    
    if req.method == 'POST':
        
        formulario_edit_user = UserEditForm(req.POST, instance=usuario)
        
        if formulario_edit_user.is_valid():
            data = formulario_edit_user.cleaned_data
            usuario.nombre = data['nombre']
            usuario.apellido = data['apellido']
            usuario.email = data['email']
            usuario.set_password(data['password'])
            usuario.save()
            
            return render(req, 'index.html', {'mensaje':f'El Usuario {usuario} actualizado exitosamente!'})
        
        else: 
            return render(req, 'abm/update/update_user.html', {'formulario_edit_user': formulario_edit_user}, {'mensaje':'Error al actualizar usuario! Intente nuevamente'})
    
    else:
        formulario_edit_user = UserEditForm(instance=req.user)
        return render(req, 'abm/update/update_user.html', {'formulario_edit_user': formulario_edit_user})