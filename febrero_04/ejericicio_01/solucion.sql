-- SINTAXIS DE INSERT 

INSERT INTO inventario (nombre_producto,precio,cantidad_disponible) VALUES ('Laptop', 450000, 12),
('Teclado', 35000, 22);

INSERT INTO inventario (nombre_producto,precio,cantidad_disponible) VALUES ('Teclado 2', 10990, 5),
('Mouse', 5500, 10),
('Audifonos', 21990, 8);

INSERT INTO inventario (nombre_producto,precio,cantidad_disponible) 
VALUES ('Disco SSD 1TB - Samsung', 120.00, 15), 
('Memoria RAM 16GB - Corsair', 85.00, 20),  
('Procesador - Intel', 320.00, 8);

INSERT INTO inventario (nombre_producto,precio,cantidad_disponible) 
VALUES ('Pantalla', 85000, 5);

INSERT INTO inventario (nombre_producto, precio, cantidad_disponible)
VALUES
('Taladro', 45990.50, 10),
('Serrucho', 8990.00, 40),
('Clavos 2 pulgadas', 1990.00, 200);

-- transaccion para eliminar datos

begin ;

delete 
from inventario
where precio <15000;

select * from inventario
where precio <15000;

commit;
rollback;