CREATE DATABASE fsp_2025;

CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    email       VARCHAR(100),
    telefono    VARCHAR(20)
);

CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    nombre       VARCHAR(100) NOT NULL,
    precio       NUMERIC(10,2) NOT NULL
);

CREATE TABLE ordenes (
    id_orden   SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha      DATE NOT NULL,
    total      NUMERIC(10,2),

    FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
);

CREATE TABLE detalle_orden (
    id_detalle  SERIAL PRIMARY KEY,
    id_orden    INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad    INT NOT NULL,
    precio_unitario NUMERIC(10,2) NOT NULL,

    FOREIGN KEY (id_orden)
        REFERENCES ordenes(id_orden),

    FOREIGN KEY (id_producto)
        REFERENCES productos(id_producto)
);


INSERT INTO clientes (nombre, email, telefono) VALUES
('Juan Pérez', 'juan@gmail.com', '987654321'),
('María González', 'maria@gmail.com', '912345678'),
('Carlos Soto', 'carlos@gmail.com', '998877665');

INSERT INTO productos (nombre, precio) VALUES
('Notebook', 850000),
('Mouse', 15000),
('Teclado', 30000),
('Monitor', 220000);

INSERT INTO ordenes (id_cliente, fecha, total) VALUES
(1, '2026-01-10', 895000),
(2, '2026-01-12', 235000);

INSERT INTO detalle_orden (id_orden, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 1, 850000), -- Notebook
(1, 2, 3, 15000),  -- Mouse
(2, 4, 1, 220000), -- Monitor
(2, 3, 1, 30000);  -- Teclado