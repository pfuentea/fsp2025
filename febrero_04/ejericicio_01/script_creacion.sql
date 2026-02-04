CREATE TABLE inventario (
    id SERIAL PRIMARY KEY,
    nombre_producto VARCHAR(100),
    precio NUMERIC(10,2),
    cantidad_disponible INT
);

