from clases.libros import Libro
from clases.usuarios import Usuario


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def registrar_libro(self, titulo, autor, id_libro):
        nuevo_libro = Libro(titulo, autor, id_libro)
        self.libros.append(nuevo_libro)

    def registrar_usuario(self, nombre, id_usuario):
        nuevo_usuario = Usuario(nombre, id_usuario)
        self.usuarios.append(nuevo_usuario)

    def prestar_libro(self, id_usuario, id_libro):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(id_libro)
        if usuario and libro and libro.disponible:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            return f"Libro '{libro.titulo}' prestado a {usuario.nombre}"
        return "Prestamo no disponible."

    def devolver_libro(self, id_usuario, id_libro):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(id_libro)
        if usuario and libro and libro in usuario.libros_prestados:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            return f"Libro '{libro.titulo}' devuelto por {usuario.nombre}"
        return "Devolución no disponible."

    def buscar_libro(self, id_libro):
        for libro in self.libros:
            if id_libro == id_libro:
                return libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.mostrar_info())

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario.mostrar_info())
