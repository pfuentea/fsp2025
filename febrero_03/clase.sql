
-- sintaxis DELETE
-- DELETE FROM [TABLA] WHERE [CONDICION] ;
--DELETE 
select *  -- IMPORTANTE HACER UN SELECT PRIMERO!!!
from autores
WHERE  -- nombre like  'J%' -- todos los nombres que comienzan con "J"
nombre like '%a'   -- todos los nombres que terminan con una "a"


-- ELIMINAR LOS AUTORES QUE COMIENCEN CON J
DELETE
from autores
WHERE  nombre like  'J%';


select * from autores;

create table frutas(
id_fruta SERIAL PRIMARY KEY, 
nombre varchar(40),
fecha date
)

insert into frutas(nombre,fecha) 
values 
('manzana','2026-01-01') ,
('pera','2026-01-12'),
('sandia','2026-01-20'),
('uva','2026-01-26'), 
('platano','2026-01-15');

-- aliminamos todas las frutas que contengan una "a"
delete 
from frutas
where nombre like '%a%';

select * from frutas
--where fecha >='2026-01-01' AND FECHA <='2026-01-15'
--WHERE FECHA BETWEEN '2026-01-01' AND '2026-01-15'  -- between se usa para rangos 
where id_fruta between 1 and 4

-- DML=CRUD ( create-read-update-delete)

-- TRANSACCIONES 
BEGIN ;

delete 
from frutas 
where nombre like '%a';

select * from frutas;

-- COMMIT; -- confirmar cambios
 ROLLBACK;  -- deshacer los cambios

 