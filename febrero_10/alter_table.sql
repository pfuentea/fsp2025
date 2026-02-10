-- creamos 3 tablas
create table productos(
id_producto serial primary key,
nombre VARCHAR(255) not null,
valor INT not null
);
create table usuarios(
id_usuario serial primary key,
nombre varchar(255) not null,
fec_nac date 
);

create table transacciones(
id_transaccion serial primary key,
id_usuario int not null references usuarios(id_usuario),
id_producto int not null references productos(id_producto),
cantidad int not null,
valor int not null
);

-- cambiamos el nombre de la columna
ALTER TABLE productos RENAME COLUMN valor TO importe;
ALTER TABLE transacciones RENAME COLUMN valor TO importe;

select * from transacciones;

select * from productos;

-- cambiamos el tipo de dato de la columna
ALTER TABLE productos ALTER COLUMN importe TYPE decimal(10,2);
ALTER TABLE transacciones ALTER COLUMN importe TYPE decimal(10,2);

alter table usuarios add column email varchar(100);

select * from usuarios;
insert into usuarios (nombre,fec_nac,email) values('Condorito','2026-02-10','condorito@gmail.com');

update usuarios set email='' where id_usuario=1;

alter table usuarios alter column email set not null;