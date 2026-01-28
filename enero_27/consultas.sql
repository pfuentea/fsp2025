-- consultar cada tabla

select * FROM clientes;
select * FROM productos;
select * FROM ordenes;
select * FROM detalle_orden;

-- consultar los totales por tabla
select count(*) FROM clientes;
select count(*) FROM productos;
select count(*) FROM ordenes;
select count(*) FROM detalle_orden;

-- consultar el producto con el precio más alto


select nombre, precio 
from productos
where precio = (select max (precio) from productos);

select *
FROM productos
order by precio desc 
limit 1;

