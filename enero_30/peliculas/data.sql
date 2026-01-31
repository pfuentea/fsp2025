INSERT INTO actores (nombre, apellido, genero) VALUES
('Leonardo', 'DiCaprio', 'Drama'),
('Scarlett', 'Johansson', 'Acción'),
('Keanu', 'Reeves', 'Acción'),
('Natalie', 'Portman', 'Drama'),
('Chris', 'Hemsworth', 'Acción');

INSERT INTO peliculas (titulo, genero, anio_estreno) VALUES
('Inception', 'Drama', 2010),
('Matrix', 'Acción', 1999),
('Avengers', 'Acción', 2012),
('Black Swan', 'Drama', 2010),
('John Wick', 'Acción', 2014);

INSERT INTO peliculas_actores (id_pelicula, id_actor, es_principal) VALUES
-- Inception
(1, 1, TRUE),

-- Matrix
(2, 3, TRUE),

-- Avengers
(3, 2, FALSE),
(3, 5, TRUE),

-- Black Swan
(4, 4, TRUE),

-- John Wick
(5, 3, TRUE);