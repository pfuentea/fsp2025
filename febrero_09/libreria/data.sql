
INSERT INTO Autores (nombre, nacionalidad) VALUES
('Gabriel García Márquez', 'Colombiano'),
('Isabel Allende', 'Chilena'),
('J.K. Rowling', 'Británica');

INSERT INTO Categorias (nombre_categoria) VALUES
('Novela'),
('Ciencia Ficción'),
('Fantasía');

INSERT INTO Libros (titulo, autor_id, categoria_id, precio, stock) VALUES
('Cien Años de Soledad', 1, 1, 25.99, 20),
('La Casa de los Espíritus', 2, 1, 19.99, 15),
('Harry Potter y la Piedra Filosofal', 3, 3, 29.99, 30);


INSERT INTO Ventas (libro_id, cantidad) VALUES
(1, 2),
(3, 1),
(2, 4);

SELECT * FROM Autores;
SELECT * FROM Categorias;
SELECT * FROM Libros;
SELECT * FROM Ventas;