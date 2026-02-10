create database libreria;

create table autores (
	autor_id serial primary key,
	nombre varchar(100) not null,
	nacionalidad varchar(50)
);

create table categorias(
	categoria_id serial primary key,
	nombre_categoria varchar(60) not null
);

create table libros(
	libro_id serial primary key,
	titulo varchar(60) not null,
	autor_id int not null references autores(autor_id) on delete cascade, 
	categoria_id int not null references categorias(categoria_id) on delete cascade,
	precio decimal (10,2) not null,
	stock int not null default 0 check (stock >=0)
);

create table ventas(
	venta_id serial primary key,
	libro_id int not null references libros(libro_id) on delete cascade,
	cantidad int not null check (cantidad >0),
	fecha_venta date not null default current_date
);

