from django.urls import path
from django.contrib.auth.views import LogoutView
from book_loans.views import delete_book, index, lista_autores, lista_clientes, lista_libros, lista_prestamos, nuevo_autor, nuevo_cliente, nuevo_libro, nuevo_prestamo, registro_usuario, update_book, user_login


urlpatterns = [
    path('', index , name='index'),
    path('nuevo_prestamo/', nuevo_prestamo, name='nuevo_prestamo'),
    path('lista_prestamos/', lista_prestamos, name='lista_prestamos'),
    path('lista_libros/', lista_libros, name='lista_libros'),
    path('lista_autores/', lista_autores, name='lista_autores'),
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
    path('nuevo_autor/', nuevo_autor, name='nuevo_autor'),
    path('nuevo_cliente/', nuevo_cliente, name='nuevo_cliente'),
    path('nuevo_libro/', nuevo_libro, name='nuevo_libro'),
    path('user_login/', user_login, name='user_login'),
    path('resgistro/', registro_usuario, name='registro'),
    path('logout/', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('delete_book/<int:id>', delete_book, name='delete_book'),
    path('update_book/<int:id>', update_book, name='update_book'),
    path('update_user/', edit_user, name='update_user'),
]
