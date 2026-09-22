from libreria import agregar_libro, listar_libros, libros_por_autor, existe_libro

# Añade una colección de libros
coleccion = [
    agregar_libro("El señor de los anillos", "J.R.R. Tolkien"),
    agregar_libro("El hobbit", "J.R.R. Tolkien"),
    agregar_libro("1984", "George Orwell"),
    agregar_libro("Dune", "Frank Herbert")
]

# Muestra la colección de libros creada
print("Colección de libros:")
print(listar_libros(coleccion))

# Busca un libro por el autor
print("\nLibros de J.R.R. Tolkien:")
print(libros_por_autor(coleccion, "J.R.R. Tolkien"))

# Verifica si un libro está disponible
print("\n¿Está disponible '1984'?")
print(existe_libro(coleccion, "1984"))

print("\n¿Está disponible 'Fundación'?")
print(existe_libro(coleccion, "Fundación"))