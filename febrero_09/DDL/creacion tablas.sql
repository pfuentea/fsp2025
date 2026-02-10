-- creación de tabla CREATE TABLE
CREATE TABLE monedas (
	currency_id SERIAL PRIMARY KEY,
	currency_name VARCHAR(50),
	currency_sumbol VARCHAR(10)
);

-- revisar como quedo (estructura)
select * from monedas;

-- creacion de tablas con distintos tipos de datos
create table libros(
    id serial primary key,
    titulo varchar(100),
    autor varchar(50),
    ano_publicacion int,
    disponible boolean
);

insert into libros (titulo,autor,ano_publicacion,disponible)
values('Señor de los anillos','Tolien',1929,True);


insert into libros (titulo,autor,ano_publicacion,disponible)
values('Señor de los anillos','Tolien',1929, FALSE);

select * from libros;

create table categorias (
	id_categoria serial primary key,
	nombre_categoria varchar(50)
);

-- creacion de tabla con restricciones
drop table if exists productos;

create table productos(
	id_producto serial primary key,
	nombre_producto varchar(50),
	precio decimal(10,2) ,
	id_categoria int references categorias(id_categoria)
);

insert into categorias(nombre_categoria) values ('Lacteos'),('Cecinas'),('Embutidos');

select * from categorias;

insert into productos (nombre_producto,precio,id_categoria) 
Values ('Yogurt',250,1), ('Vienesas',3000,2),('Longaniza',4000,3);

select * from productos;

insert into productos (nombre_producto,precio,id_categoria) 
Values ('Helado',null ,1);
--antes de agregar la restrición, debemos limpiar la data 
-- para que no existan registos NULL en el campo

delete from productos where precio is null;
-- agregamos la restricion a la columna modificando la tabla
ALTER TABLE productos
ALTER COLUMN precio SET NOT NULL;

-- intentamos agregar un dato con error

insert into productos (nombre_producto,precio,id_categoria) 
Values ('Helado',null ,1);