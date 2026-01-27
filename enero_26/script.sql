CREATE DATABASE fsp_2025;


CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    email       VARCHAR(100),
    telefono    VARCHAR(20)
);

INSERT INTO clientes (nombre, email, telefono) VALUES
('Juan Pérez', 'juan@gmail.com', '987654321'),
('María González', 'maria@gmail.com', '912345678'),
('Carlos Soto', 'carlos@gmail.com', '998877665');


SELECT nombre, 
UPPER(nombre) AS nombre_en_mayuscula , 
LENGTH(nombre) AS largo_nombre
FROM clientes


WHERE UPPER(nombre) = 'CARLOS SOTO'
order by id_cliente desc


where (telefono like '9%2%' or nombre like '%J%')
and telefono like '%8%'
order by nombre desc
