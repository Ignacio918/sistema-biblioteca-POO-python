class Libro:
    def __init__(self, titulo, autor, id_libro, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.id_libro = id_libro
        self.disponible = disponible

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Titulo: {self.tituo}, Autor: {self.autor}, ID: {self.id_libro}, Estado: {estado}"
