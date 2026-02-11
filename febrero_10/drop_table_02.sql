create database almacen;

CREATE TABLE Productos (
	id_producto SERIAL PRIMARY KEY ,
	nombre VARCHAR(100) NOT NULL,
	precio DECIMAL(10,2) NULL,
	stock INT DEFAULT 0
);

INSERT INTO Productos (nombre, precio, stock) VALUES
('Laptop', 1200.50, 10),
('Mouse', 25.75, 50),
('Teclado', 45.30, 30);

SELECT * FROM Productos;

alter table productos alter column precio set not null;

INSERT INTO Productos (nombre, stock) VALUES ('Monitor', 20);

drop table productos;
