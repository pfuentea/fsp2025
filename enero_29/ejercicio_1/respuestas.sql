-- 1. Género menos frecuente
select titulo
from libros
where id_genero = (select id_genero
				from libros
				group by id_genero
				order by count(*) asc
				limit 1
				)

-- 2 Autores “prolíficos recientes”
select nombre, apellido
from autores
where id_autor in (
	select id_autor
	from libros
	where anio_publicacion > (select avg(anio_publicacion) 
							from libros)
)

-- Top-3 géneros por cantidad de libros

select 
l.id_genero 
, count(l.titulo)
from libros as l
group by l.id_genero
order by count(l.titulo) desc
limit 3;

select g.nombre_genero from generos as g where g.id_genero =1;

select 
(select g.nombre_genero 
from generos as g 
where g.id_genero =l.id_genero ) as nombre_genero
, count(l.titulo) cantidad_libros
from libros as l
group by l.id_genero
order by count(l.titulo) desc
limit 3;