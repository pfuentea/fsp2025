CREATE TABLE actores (
    id_actor SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    genero VARCHAR(50) NOT NULL
);

CREATE TABLE peliculas (
    id_pelicula SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    anio_estreno INT NOT NULL CHECK (anio_estreno >= 1900)
);

CREATE TABLE peliculas_actores (
    id_pelicula INT NOT NULL,
    id_actor INT NOT NULL,
    es_principal BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (id_pelicula, id_actor),
    CONSTRAINT fk_pelicula
        FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula),
    CONSTRAINT fk_actor
        FOREIGN KEY (id_actor) REFERENCES actores(id_actor)
);