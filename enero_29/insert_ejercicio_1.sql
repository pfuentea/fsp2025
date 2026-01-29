
INSERT INTO autores (nombre, apellido) VALUES
('Gabriela', 'Mistral'),
('Pablo', 'Neruda'),
('Isabel', 'Allende'),
('Jorge', 'Borges'),
('Julio', 'Cortázar'),
('Mario', 'Vargas Llosa'),
('Haruki', 'Murakami'),
('Ursula', 'Le Guin'),
('Agatha', 'Christie'),
('Stephen', 'King');

INSERT INTO generos (nombre_genero) VALUES
('Fantasía'),
('Ciencia Ficción'),
('Misterio'),
('Romance'),
('Historia'),
('Poesía'),
('Terror'),
('Filosofía'),
('Aventura'),
('Tecnología');
INSERT INTO libros (titulo, anio_publicacion, id_genero, id_autor) VALUES
('La casa de los espíritus', 1982, 4, 3),
('Veinte poemas de amor', 1924, 6, 2),
('Ficciones', 1944, 8, 4),
('Rayuela', 1963, 9, 5),
('It', 1986, 7, 10),
('Asesinato en el Orient Express', 1934, 3, 9),
('El Aleph', 1949, 8, 4),
('Tokio Blues', 1987, 4, 7),
('Kafka en la orilla', 2002, 1, 7),
('La mano izquierda de la oscuridad', 1969, 2, 8),
('El resplandor', 1977, 7, 10),
('Diez negritos', 1939, 3, 9),
('Canto general', 1950, 6, 2),
('Desolación', 1922, 6, 1),
('La ciudad y los perros', 1963, 5, 6),
('Crónica de una muerte anunciada', 1981, 3, 5),
('El viento canta', 2019, 1, 7),
('Sombras digitales', 2022, 10, 6), -- único libro de Tecnología
('El nombre del viento', 2007, 1, 8),
('El misterio del reloj', 2021, 3, 9);