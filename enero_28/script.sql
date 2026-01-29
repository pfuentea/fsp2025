
-- como buscar clientes con id 2 ^ 4 
select * 
FROM clientes
WHERE id_cliente = 2 
or id_cliente = 4
;

select * 
FROM clientes
WHERE id_cliente in (2,4) 
;

-- nombre y pais de las personas que hicieron al menos una orden en el 2025
select nombre, pais
FROM clientes
WHERE id_cliente in (select id_cliente
					from ordenes
					where fecha >= '2025-01-01'
					  and fecha < '2026-01-01'
					);
-- Obtener los nombres de los productos y la suma total vendida (cantidad × precio).
select 
	(select p.nombre 
	from productos as p
	where p.id_producto=o.id_producto) as producto
	,
	-- cantidad,
	-- precio_unitario,
	sum(o.cantidad*o.precio_unitario) as total_vendido
from detalle_orden as o
group by o.id_producto
;
-- Listar el nombre del cliente y el monto total comprado, ordenados de mayor a menor.

select cli.nombre, 
-- ord.id_cliente, det.id_orden, 
sum(det.cantidad*det.precio_unitario) as total_vendido
from detalle_orden as det
join ordenes as ord on ( ord.id_orden = det.id_orden )
join clientes as cli on (cli.id_cliente = ord.id_cliente )
group by cli.nombre
-- ,ord.id_cliente, det.id_orden
order by total_vendido desc , cli.nombre asc;

-- Contar cuántos clientes distintos hicieron compras en cada país.
select pais, count(*) as cantidad
from clientes
where id_cliente in (
		select id_cliente
		from ordenes
		)
group by pais
;