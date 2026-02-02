CREATE TABLE autores (
    id_autor SERIAL PRIMARY KEY,
    nombre   VARCHAR(60) NOT NULL,
    apellido VARCHAR(60) NOT NULL
);

CREATE TABLE generos (
    id_genero SERIAL PRIMARY KEY,
    nombre_genero VARCHAR(80) NOT NULL UNIQUE
);
CREATE TABLE editoriales (
    id_editorial      SERIAL PRIMARY KEY,
    nombre_editorial  VARCHAR(100) NOT NULL UNIQUE,
    pais              VARCHAR(60)
);

CREATE TABLE libros (
    id_libro          SERIAL PRIMARY KEY,
    titulo            VARCHAR(150) NOT NULL,
    anio_publicacion  INT NOT NULL
        CHECK (anio_publicacion BETWEEN 1800 AND EXTRACT(YEAR FROM CURRENT_DATE)::INT),
    id_genero         INT NOT NULL,
    id_autor          INT NOT NULL,
    id_editorial      INT NOT NULL,

    CONSTRAINT fk_libros_genero
        FOREIGN KEY (id_genero) REFERENCES generos(id_genero),
    CONSTRAINT fk_libros_autor
        FOREIGN KEY (id_autor) REFERENCES autores(id_autor),
    CONSTRAINT fk_libros_editorial
        FOREIGN KEY (id_editorial) REFERENCES editoriales(id_editorial)
);