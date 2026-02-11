
create view vw_autores_chilenos as
select nombre, nacionalidad
from autores
where nacionalidad='Chilena'


select * from  vw_autores_chilenos


drop view vw_autores_chilenos;

create or replace view vw_autores_chilenos as
select a.nombre, l.titulo
from autores as a
left join libros as l on (l.autor_id=a.autor_id)
where a.nacionalidad='Chilena';