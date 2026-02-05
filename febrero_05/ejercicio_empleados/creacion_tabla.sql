CREATE TABLE empleados (
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    salario NUMERIC(10,2),
    fecha_ingreso DATE,
    departamento VARCHAR(50)
);