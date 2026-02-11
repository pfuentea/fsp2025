
insert into usuarios (nombre,fec_nac) values('Condorito','2026-02-10');
insert into productos(nombre,valor) values ('pan',2000);

insert into transacciones(id_usuario,id_producto,cantidad,valor)
values (1,1,2,1000);

-- truncado de tabla de forma segura
begin;
truncate table usuarios CASCADE;
select * from usuarios;
select * from transacciones;
rollback;

select * from usuarios;
select * from transacciones;