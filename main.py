from clases.biblioteca import Biblioteca


def main():
    biblioteca = Biblioteca()
    while True:
        print("\n --- Menú Biblioteca Cuerva ---")
        print("1. Registrar un libro")
        print("2. Registrar un usuario")
        print("3. Prestar un libro")
        print("4. Devolver un libro")
        print("5. Mostrar libros")
        print("6. Mostrara usuarios")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ").lower()
            autor = input("Ingrese el autor del libro: ").lower()
            id_libro = input("Ingrese el ID del libro: ").lower()
            biblioteca.registrar_libro(titulo, autor, id_libro)
            print(f"Libro '{titulo}' registrado con éxito.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ").lower()
            id_usuario = input("Ingrese el ID del usuario: ").lower()
            biblioteca.registrar_usuario(nombre, id_usuario)
            print(f"Usuario '{nombre}' registrado con éxito.")

        elif opcion == "3":
            id_usuario = input("Ingrese el nombre del usuario: ").lower()
            id_libro = input("Ingrese el ID del Libro a prestar: ").lower
            print(biblioteca.prestar_libro(id_usuario, id_libro))

        elif opcion == "4":
            id_usuario = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            print(biblioteca.devolver_libro(id_usuario, isbn))

        elif opcion == "5":
            biblioteca.mostrar_libros()

        elif opcion == "6":
            biblioteca.mostrar_usuarios()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main()
