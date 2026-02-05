
-- destruye la casa completa
drop table transferencias;

-- elimina toda la informacion de la tabla (borra todo lo que esta dentro de la casa)
truncate transferencias;

-- elimina solo las cosas de una habitación
delete from transferencias where CONDICION
